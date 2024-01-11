#!/usr/bin/node

// This script defines a class Rectangle that represents a rectangle with width and height properties.

class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
