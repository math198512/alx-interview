#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.hbtn.io/api/films/';

const filmId = process.argv[2];

const API_URL = BASE_URL + filmId;
request(API_URL, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const json = JSON.parse(body);
    const characList = json.characters; // Handle the response body
    const promises = characList.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (error1, response1, body1) => {
          if (!error1 && response1.statusCode === 200) {
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
});
