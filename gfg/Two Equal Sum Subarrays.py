'''
Two Equal Sum Subarrays
Difficulty: Easy    Accuracy: 54.45%    Submissions: 50K+    Points: 2    Average Time: 15m
Given an array of integers arr[], return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.

Example 1:
Input: arr[] = [1, 2, 3, 4, 5, 5]
Output: true
Explanation: We can divide the array into [1, 2, 3, 4] and [5, 5]. The sum of both the subarrays are 10.


Example 2:
Input: arr[] = [4, 3, 2, 1]
Output: false
Explanation: We cannot divide the array into two subarrays with equal sum.

Constraints:
1 ≤ arr.size() ≤ 105 
1 ≤ arr[i] ≤ 106
'''

class Solution:
    def canSplit(self, arr):
        total = sum(arr)
        
        # If total sum is odd, cannot split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        curr_sum = 0
        
        # Check if any prefix sum becomes equal to half
        for num in arr:
            curr_sum += num
            if curr_sum == target:
                return True
        
        return False