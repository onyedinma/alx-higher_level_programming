#!/usr/bin/node

// This script defines a function that calls another function a specified number of times and exports it.

// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  // Call theFunction x times using a for loop
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function
exports.callMeMoby = callMeMoby;
