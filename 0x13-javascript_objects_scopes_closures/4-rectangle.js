#!/usr/bin/node

// Define the Rectangle class.
module.exports = class Rectangle {
  // The constructor for the Rectangle class.
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  // Print the rectangle.
  print (char = 'X') {
    for (let i = 0; i < this.height; ++i) {
      let j = 0;

      for (; j < this.width; ++j) {
        process.stdout.write(char);
      }

      if (j === this.width) {
        console.log('');
      }
    }
  }

  // Rotate the rectangle.
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Double the width and height of the rectangle.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
