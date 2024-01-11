#!/usr/bin/node

// Import the OldSquare class from './5-square'
const OldSquare = require('./5-square');

// Define the Square class that extends the OldSquare class
module.exports = class Square extends OldSquare {
  constructor (size) {
    // Call the super constructor of the OldSquare class with size as both the width and height
    super(size, size);
  }

  double () {
    // Call the super.double() method from the OldSquare class
    super.double();
  }

  charPrint (c = 'X') {
    // Call the super.print(c) method from the OldSquare class
    super.print(c);
  }
};
