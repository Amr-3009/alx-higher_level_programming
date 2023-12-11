#!/usr/bin/node
// random px

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const list = process.argv.slice(2).map(Number).sort();
  console.log(list.reverse()[1]);
}
