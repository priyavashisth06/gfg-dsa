'''
URLify a given string
Difficulty: Basic    Accuracy: 60.18%    Submissions: 13K+    Points: 1


Given a string s, replace all the spaces in the string with '%20'.

Example 1:
Input: s = "i love programming"
Output: "i%20love%20programming"
Explanation: The 2 spaces are replaced by '%20'


Example 2:
Input: s = "Mr Benedict Cumberbatch"
Output: "Mr%20Benedict%20Cumberbatch"
Explanation: The 2 spaces are replaced by '%20'


Constraints:
1 ≤ s.size() ≤ 104
'''


#User function Template for python3
class Solution:
    def urlify(self, s):
        return s.replace(" ", "%20")