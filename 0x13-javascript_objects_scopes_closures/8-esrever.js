#!/usr/bin/node

// Reverses the elements in a list
exports.esrever = function (list) {
  const reverList = [];

  // Iterate over the list in reverse order
  for (let i = list.length - 1; i >= 0; --i) {
    // Push each element to the revList array
    reverList.push(list[i]);
  }

  // Return the reversed list
  return reverList;
};
