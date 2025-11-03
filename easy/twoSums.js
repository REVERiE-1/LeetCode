
/*

For this exercise, we are given two arguments from the param. First is an array of nums and the second is a target number to reach.
We need to find the pair of numbers to reach the target number and return their indices in an array.
We can assume in this exercise that there's always one solution and we cannot use the same element twice.

My approach is this particular case is to brute force it. Using a double for loop to check for every possible sum of pair of numbers OR until we find the correct one,
Then retreive their indices and return in the form of an array.

A very straightforward solution for this one. 
*/ 

/**
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
    let maxSum = 0;
    let correctNum = 0;
    let correctPair = [];
    for (let i = 0;i<nums.length;i++){
        for (let j = i+1;j<nums.length;j++){
            correctNum = nums[i] + nums[j];
            if (correctNum === target){
                correctPair.push(i,j);
                break;
            }
        }   
    }
    return correctPair;
}
