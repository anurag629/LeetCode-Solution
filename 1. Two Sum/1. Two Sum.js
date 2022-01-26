/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let clues = {};

    for (let i = 0; i < nums.length; i++) {        
        
        // if a previous element needs this value
        if (nums[i] in clues) {
            return [clues[nums[i]], i];
        }

        // save the clue to check later
        clues[target - nums[i]] = i;
    }
    return [];
};