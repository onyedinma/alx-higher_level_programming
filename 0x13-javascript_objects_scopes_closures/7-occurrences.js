#!/usr/bin/node

// This script defines a function that returns the number of occurrences of an element in a list.

function nbOccurences (list, searchElement) {
  // Filter the list to only include elements that are equal to the search element
  const filteredList = list.filter(x => x === searchElement);

  // Return the length of the filtered list, which is the number of occurrences of the search element
  return filteredList.length;
}
// Export the nbOccurences function
exports.nbOccurences = nbOccurences;
