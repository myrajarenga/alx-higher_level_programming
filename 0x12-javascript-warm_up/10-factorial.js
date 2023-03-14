#!/usr/bin/node

function factorial (n) {
  // Base case: factorial of 0 or 1 is 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: factorial of n is n times factorial of n-1
  return n * factorial(n - 1);
}

// Get the first argument from the command line and compute its factorial
const arg = parseInt(process.argv[2]);
const result = isNaN(arg) ? 1 : factorial(arg);

// Print the result
console.log(result);
