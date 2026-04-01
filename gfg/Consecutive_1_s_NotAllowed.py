""" Consecutive 1's not allowed
Difficulty: MediumAccuracy: 27.46%Submissions: 128K+Points: 4


Given a positive integer n, count all possible distinct binary strings of length n such that there are no consecutive 1's.

Example 1:
Input: n = 3
Output: 5
Explanation: 5 strings are ("000", "001", "010", "100", "101").

Example 2:
Input: n = 2
Output: 3
Explanation: 3 strings are ("00", "01", "10").

Example 3:
Input: n = 1
Output: 2


Constraints:
1 ≤ n ≤ 44 """


class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2
        
        prev2, prev1 = 2, 3 
        
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        
        return prev1