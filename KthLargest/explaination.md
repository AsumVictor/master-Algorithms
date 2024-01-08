# CHALLENGE
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

# EXPLAINATION
input arrays of numbers
output: number

For return kth largest element of numbers arrays
for example if I have an array of numbers 
1,2,3,4,5,6,3,6,5,4,3
and I'm to present 3rd largest

that means I should return 4

I should present only 3rd number from a sorted array not like may 
6,6,5,5,4,4,3....
I should return 5 because it is in the 3rd position.


# PROCESS
 I should group all numbers as one 
example io have 
6
5
4
...
then return the kth

therefore i will save the numbers 
For this I will use hash table to store the numbers as key and freq as value.

the I will sort the table according keys in decending order and then 

return the slice of k

# SUDO-CODE
Store arrays in a set to get unique value
sort the set according to decending the order
slice from K, k+1

Time complexity 
:
logn