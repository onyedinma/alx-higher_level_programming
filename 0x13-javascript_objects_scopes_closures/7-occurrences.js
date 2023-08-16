#!/usr/bin/node
// Returns the number of occurrences of an element in a list
exports.nbOccurrences = function (list, searchElement) {
  // Using the filter() method to create a new array with only the elements that match the searchElement
  // Then, using the length property to get the number of elements in the filtered array
  return list.filter(x => x === searchElement).length;
};
