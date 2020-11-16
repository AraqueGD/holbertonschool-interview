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
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    for (const character of movie.characters) {
      request(character, function (error2, response, body2) {
        if (error) {
          console.error(error2);
        } else {
          const person = JSON.parse(body2);
          console.log(person.name);
        }
      });
    }
  }
});