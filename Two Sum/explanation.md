# Problem 
   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
   You may assume that each input would have exactly one solution, and you may not use the same element twice.
   You can return the answer in any order.

# Explaination
  - Input data: Arrays of integers 
  - Output: arrays of numbers
  - An arrays with number and should pick first two numbers to that add up to the target
# Process
  - declare empty hashmap
  - loop through the arrays 
  - check if the current element is in the hashmap get the return both the value and the index of the current element
  - else store the complement of the current element as the key and the index as value.
# Test cases
 Example 
 ARRAY: 1,3,6,8,4,5,9,4,3
 TARGET: 6
 ANSWER: [0, 4]

loop 

