#!/usr/bin/node
// Factorial in Javascript

function factorial (num) {
  if (isNaN(num) || num < 2) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
