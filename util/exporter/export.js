const file_out = 'database_new.csv';
const mongodb = require("mongodb").MongoClient;
const fastcsv = require("fast-csv");
const fs = require("fs");
const ws = fs.createWriteStream(file_out);

// let url = "mongodb://username:password@localhost:27017/";
let url = "mongodb://localhost:27017/";

mongodb.connect(
    url,
    { useNewUrlParser: true, useUnifiedTopology: true },
    (err, client) => {
        if (err) throw err;

        client
            .db("thesis")
            .collection("dumps")
            .find({Timestamp: /22-01-2020.*/})
            .toArray((err, data) => {
                if (err) throw err;

                // console.log(data);
                fastcsv
                    .write(data, { headers: true })
                    .on("finish", function() {
                        console.log(`Write ${file_out} successfully!`);
                    })
                    .pipe(ws);

                client.close();
            });
    }
);
