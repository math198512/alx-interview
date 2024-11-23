#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/3/';


request(API_URL, (error, response, body) => {
    if (!error && response.statusCode == 200) {
        let json = JSON.parse(body);
        const charac_list = json.characters;  // Handle the response body
        for (let i = 0; i < charac_list.length; i++) {
            request(charac_list[i], (error1, response1, body1) => {
                if (!error1 && response1.statusCode == 200) {
                    console.log(JSON.parse(body1).name)
                }
            })
        }
    }
})
