#!/usr/bin/node

'use strict';

function factorial(n) {
  const num = parseInt(n);
  if (isNaN(num)) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(process.argv[2]));
