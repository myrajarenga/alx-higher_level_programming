#!/usr/bin/node

// check if any arguments are passed
if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  // convert arguments to integers
  const integers = process.argv.slice(2).map(arg => parseInt(arg, 10));
  // sort the integers in descending order
  integers.sort((a, b) => b - a);
  // find the second biggest integer
  const secondBiggest = integers[1];
  console.log(secondBiggest);
}
