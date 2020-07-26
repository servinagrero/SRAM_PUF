#include <iostream>
#include <fstream>
#include <string>
#include <ranges>
#include <functional>
#include <sstream>
#include <exception>
#include <atomic>
#include <filesystem>
#include <limits>
#include <typeinfo>
#include <map>

#include <nlohmann/json.hpp>
using json = nlohmann::json;

// Extract values from a line in a file whose values are separated by sep
// Used to extract the board names
std::vector<std::string> read_delim_file(std::string filename, char sep=',')
{
        std::ifstream file;
        file.open(filename);
        if(!file.good()) throw std::invalid_argument("File does not exists.");

        std::vector<std::string> contents;
        std::string line;

        while(getline(file, line)){
                std::stringstream   linestream(line);
                std::string         value;

                while(getline(linestream,value,sep))
                        contents.push_back(value);
        }
        return contents;

}

// Get the files from a directory and sort them alphabetically
std::vector<std::string> get_sorted_files(std::string path)
{
        std::vector<std::string> files;

        for (auto& entry: std::filesystem::directory_iterator(path)) {
                if (!entry.is_regular_file()) continue;
                std::filesystem::path file = entry.path().string();
                files.push_back(file);
        }
        sort(files.begin(), files.end());
        return files;
}

// Extract only one sample of the given board from the samples json
std::vector<int8_t> lookup_one_sample(std::string board, json &jf)
{
        std::vector<int8_t> sample;
        for (auto& element : jf) {
                if(element["Board"] != board) continue;
                std::vector<int8_t>data = element["Data"].get<std::vector<int8_t>>();
                for(auto const& bit : data) sample.push_back(bit);
                break;
        }
        return sample;
}

// Given a board, extract a memory dump from the samples and store it in a 32*4096 vector
std::vector<int8_t> obtain_memory(std::string board, std::string path="../data/raw/32")
{
        std::vector<int8_t> memory;

        auto mem_files = get_sorted_files(path);

        for(auto& file: mem_files) {
                std::ifstream ifile(file);
                json jf = json::parse(ifile);
                auto sample = lookup_one_sample(board, jf);
                memory.insert(memory.end(), sample.begin(), sample.end());
    }

    return memory;
}

// Calculate the sum of all the weights in the weight matrix
// Since the matrix is symetric, we only need to calculate half of it
template <class Weight_fn>
double add_weights(Weight_fn weight_fn, size_t rows=131072)
{
        std::atomic<double> result(0);
        #pragma openmp parallel for collapse(2)
        for(size_t i = 1; i < rows; ++i)
                for(size_t j = 0; j < rows - 1; ++j)
                        result = result + weight_fn(i,j);

        return result;
}

// Calculate the Moran's I for the memory of a given board
template<class Weight_fn>
float morans_i(std::string board, float weights_sum, Weight_fn weight_fn,
               std::vector<int8_t> &memory = {})
{
        if(memory.size() == 0)
                memory = obtain_memory(board);

        int num_bits = memory.size(); // Should be 131072
        float x_mean = std::accumulate(memory.begin(), memory.end(), 0.0) / num_bits;

        std::atomic<float> variance(0.0);
        #pragma openmp parallel for
        for(size_t i = 0; i < memory.size(); ++i)
                variance = variance + (memory.at(i) - x_mean) * (memory.at(i) - x_mean);

        std::atomic<float> denominator(0.0);
        #pragma openmp parallel for collapse(2)
        for (size_t i = 0; i < memory.size(); i++) {
                for (size_t j = 0; j < memory.size(); j++) {
                        denominator = denominator + (weight_fn(i, j) * (memory.at(i) - x_mean) * (memory.at(j) - x_mean));
                }
        }

        std::cout << "Num bits " << num_bits << "\n"
                  << "X mean " << x_mean << "\n"
                  << "Weights sum " << weights_sum << "\n"
                  << "Denominator " << denominator << "\n"
                  << "Variance " << variance << "\n";
        return (num_bits / weights_sum) * (denominator / variance);
}

// In this case, we have as many I as there are bits
template<class Weight_fn>
std::vector<float> local_morans_i(std::string board, float weigth_sum, Weight_fn weigth_fn,
                                  std::vector<int8_t> &memory = {})
{
        if(memory.size() == 0)
                memory = obtain_memory(board);

        return {};
}

int main(int argc, char **argv)
{
        std::cout.precision(10);

        auto weight_taxi = [](int i, int j){return abs(i-j) == 1 ? 1 : 0;};
        auto weight_decay = [](int i, int j){return i == j ? 0 : 1.0/(i+j);};
        auto weight_row = [](int i, int j){return abs(i - j) < 32 ? 1 : 0;};

        std::unordered_map<std::string,  float> weight_values;

        // TODO: Cache the results since this takes a lot of time
        std::cout << "Calculating weights\n";
        weight_values.insert ( std::pair<std::string,float>("taxi",  add_weights(weight_taxi)) );
        weight_values.insert ( std::pair<std::string,float>("decay", add_weights(weight_decay)) );
        weight_values.insert ( std::pair<std::string,float>("row",   add_weights(weight_row)) );
        std::cout << "Finished calculating weights\n";

        auto boards_32 = read_delim_file("../data/interim/boards_32.csv");

        std::string board_t = boards_32[10];
        auto memory = obtain_memory(board_t);

        float I = 0.0;
        for( auto const& [weight_type, weight_sum] : weight_values ){
                I = morans_i(board_t, weight_sum, weight_decay, memory);
                std::cout << "I " << weight_type << I << "\n\n";
        }
}
