#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/3/';


request(API_URL, (error, response, body) => {
    if (!error && response.statusCode == 200) {
        let json = JSON.parse(body);
        const charac_list = json.characters;  // Handle the response body
        const promises = charac_list.map(url => {
            return new Promise((resolve, reject) => {
                request(url, (error1, response1, body1) => {
                    if (!error1 && response1.statusCode == 200) {
                        resolve(JSON.parse(body1).name);
                    } else {
                        reject(error1);
                    }
                });
            });
        });

        Promise.all(promises)
            .then(names => {
                names.forEach(name => console.log(name));
            })
            .catch(error => console.error(error));
    }
})
