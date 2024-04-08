#!/usr/bin/node

'use strict';

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 && arg2) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log('Please provide two arguments');
}
