'''Segregate 0s and 1s

Difficulty: Easy    Accuracy: 54.25%    Submissions: 155K+    Points: 2    Average Time: 15m
Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Example 1:
Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].


Example 2:
Input: arr[] = [1, 1]
Output: [1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1]

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 1
'''


class Solution:
    def segregate0and1(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            while left < right and arr[left] == 0:
                left += 1
            while left < right and arr[right] == 1:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1