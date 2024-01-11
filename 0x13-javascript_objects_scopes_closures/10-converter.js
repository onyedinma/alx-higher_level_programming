#!/usr/bin/node

// Converts a number from base 10 to another base passed as an argument using closure
exports.converter = function (base) {
  // Define the inner function myConverter
  function myConverter (n) {
    // Convert the number n to a string representation in the specified base
    return n.toString(base);
  }

  // Return the inner function myConverter
  return myConverter;
};
