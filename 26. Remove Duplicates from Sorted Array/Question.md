# 26. Remove Duplicates from Sorted Array

Given an integer array <code>nums</code> sorted in **non-decreasing order**, remove the duplicates in-place such that
each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the **first part** of the array <code>nums</code>. More formally, if there are <code>k</code> elements after removing
the duplicates, then the first <code>k</code> elements of <code>nums</code> should hold the final result. It does not
matter what you leave beyond the first <code>k</code> elements.

Return <code>k</code> after placing the final result in the first <code>k</code> slots of <code>nums</code>.

Do **not** allocate extra space for another array. You must do this by **modifying the input array** in-place with O(1)
extra memory.

## Custom Judge:

The judge will test your solution with the following code:

<code>int[] nums = [...]; // Input array

int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;

for (int i = 0; i < k; i++) {

    assert nums[i] == expectedNums[i];

}</code>

## Example 1:

<code>**Input:** nums = [1,1,2]

**Output:** 2, nums = [1,2,_]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It
does not matter what you leave beyond the returned k (hence they are underscores).</code>

## Example 2:

<code>**Input:** nums = [0,0,1,1,1,2,2,3,3,4]

**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]

**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4
respectively. It does not matter what you leave beyond the returned k (hence they are underscores).</code>

## Constraints:

* <code>0 <= nums.length <= 3 * 104</code>
* <code>-100 <= nums[i] <= 100</code>
* <code>nums</code> is sorted in **non-decreasing** order.