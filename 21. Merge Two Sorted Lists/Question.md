# 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists <code>list1</code> and <code>list2</code>.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two
lists.

Return the head of the merged linked list.

## Example 1:

![alt text](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
<code>**Input:** list1 = [1,2,4], list2 = [1,3,4]

**Output:** [1,1,2,3,4,4]</code>

## Example 2:

<code>**Input:** list1 = [], list2 = []

**Output:** []</code>

## Example 3:

<code>**Input:** list1 = [], list2 = [0]

**Output:** [0]</code>

## Constraints:

* The number of nodes in both lists is in the range <code>[0, 50]</code>.
* <code>-100 <= Node.val <= 100</code>
* Both <code>list1</code> and <code>list2</code> are sorted in **non-decreasing** order.