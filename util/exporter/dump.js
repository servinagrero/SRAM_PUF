const file_out = 'exported_64.json';
const mongodb = require("mongodb").MongoClient;
const fs = require("fs");

// let url = "mongodb://username:password@localhost:27017/";
let url = "mongodb://localhost:27017/";

mongodb.connect(
    url,
    { useNewUrlParser: true, useUnifiedTopology: true },
    (err, client) => {
        if (err) throw err;

        const query = {Type: 64};

        client
            .db("thesis")
            .collection("data")
            .find(query)
            .toArray((err, data) => {
                if (err) throw err;

                fs.writeFile(file_out, JSON.stringify(data), err => {
                        if (err) return console.error('File write error:', err)
                })

                client.close();
            });
    }
);
