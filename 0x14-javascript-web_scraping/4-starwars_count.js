#!/usr/bin/node

const request = require('request');
const swurl = process.argv[2];
let times = 0;

request(swurl, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const charId = character.split('/')[5];

      if (charId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
