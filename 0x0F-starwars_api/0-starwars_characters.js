#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie
    - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
    - Display one character name by line
    - You must use the Star wars API
    - You must use the module request
*/
const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0] + '/';
request(url, (error, response, body) => {
    if (!error) {
      const res = JSON.parse(body);
      const characters = res.characters;
      if (characters.length > 0) {
        characterRequest(0, characters[0], characters, characters.length);
      }
    } else {
      console.log(error);
    }
  });
  
  function characterRequest (idx, urlChar, characters, limit) {
    if (idx === limit) {
      return;
    }
    request(urlChar, function (error, response, body) {
      if (!error) {
        const response = JSON.parse(body);
        console.log(response.name);
        idx++;
        characterRequest(idx, characters[idx], characters, limit);
      } else {
        console.error('error:', error);
      }
    });
  }
  