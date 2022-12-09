#!/usr/bin/node
/*
    Print a square with the character #
    The size of the square must be the first argument 
    of the program.
*/

const size = parseInt(process.argv[2], 10);

if (Number.isNaN(size) || process.argv.length <= 2) {
  process.stderr.write("Usage: ./1-print_square.js <size>\n");
  process.stderr.write("Example: ./1-print_square.js 8\n");
  process.exit(1);
}

const row = "#".repeat(size);

for (let i = 0; i < size; i++) {
  process.stdout.write(row + "\n");
}
