#!/usr/bin/node
// random post

function factorial (a) {
  if ((isNaN(a)) || (a === 1)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
