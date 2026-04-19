'''
Check for Power
Difficulty: Basic    Accuracy: 34.59%    Submissions: 66K+    Points: 1

Given two positive integers x and y, determine if y is a power of x. If y is a power of x, return true. Otherwise, return false.

Example 1:
Input: x = 2, y = 8
Output: true 
Explanation: 23 is equal to 8.


Example 2:
Input: x = 1, y = 8
Output: false
Explanation: Any power of 1 is not equal to 8.


Example 3:
Input: x = 46, y = 205962976
Output: true
Explanation: 465 is equal to 205962976.


Example 4:
Input: x = 50, y = 312500000
Output: true
Explanation: 505 is equal to 312500000.


Constraints:
1 ≤ x ≤ 103
1 ≤ y ≤ 109
'''



class Solution:
    def isPower(self, x, y):
        if x == 1:
            return y == 1
    
        pow = 1
        while pow < y:
            pow *= x
    
        return pow == y
