#!/usr/bin/node

if (isNaN(Math.trunc(process.argv[2]))) {
  console.log('Missing number of occurnces');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C s fun');
  }
}
