#!/usr/bin/node
/**
 * function to count number of occurrences in a list
 * @param {list} list - list ti examine
 * @param {number} searchElement - element to search
 * @returns {number} - the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      count++;
    }
  });
  return count;
};