/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int peak = findPeakElement(mountainArr);
        int firstTry = orderBinarySearch(mountainArr, target, 0, peak);
        if (firstTry != -1) {
            return firstTry;
        } else {
            return orderBinarySearch(mountainArr, target, peak + 1, mountainArr.length() - 1);
        }
    }

    private int findPeakElement(MountainArray arr) {
        int start = 0;
        int end = arr.length() - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (arr.get(mid) < arr.get(mid + 1)) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }

    private int orderBinarySearch(MountainArray arr, int target, int start, int end) {
        boolean asc = arr.get(start) < arr.get(end);
        while (start <= end) {
            int mid = start + (end - start) / 2;
            int midValue = arr.get(mid);
            if (target == midValue) {
                return mid;
            } else if ((asc && target < midValue) || (!asc && target > midValue)) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
}
