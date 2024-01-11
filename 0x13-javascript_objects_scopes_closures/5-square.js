#!/usr/bin/node

// Import the Rectangle class from './4-rectangle'
const Rectangle = require('./4-rectangle');

// Define the Square class that extends the Rectangle class
module.exports = class Square extends Rectangle {
  constructor (size) {
    // Call the super constructor of the Rectangle class with size as both the width and height
    super(size, size);
  }

  double () {
    // Call the super.double() method from the Rectangle class
    super.double();
  }
};
