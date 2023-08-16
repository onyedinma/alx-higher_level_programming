#!/usr/bin/node

// Initialize a counter variable
let counter = 0;

// Log an item with a counter prefix
exports.logMe = function count (item) {
  // Print the counter value and the item to the console
  console.log(`${counter}: ${item}`);

  // Increment the counter by 1
  counter += 1;
};
