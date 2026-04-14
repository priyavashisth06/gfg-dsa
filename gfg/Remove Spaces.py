'''
Remove Spaces
Difficulty: Basic    Accuracy: 49.21%    Submissions: 92K+    Points: 1

Given a string s, remove all the spaces from the string and return the modified string.


Example 1:
Input: s = "g eeks for ge eks"
Output: "geeksforgeeks"
Explanation: All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "geeksforgeeks".


Example 2:
Input: s = "abc d "
Output: "abcd"
Explanation:  All space characters are removed from the given string while preserving the order of the remaining characters, resulting in the final string "abcd".


Constraints:
1 ≤ |s| ≤ 105
'''


#Solution 1
class Solution:
    def removeSpaces(self, s):
        return s.replace(" ", "")
    


#Solution 2
class Solution:
    def removeSpaces(self, s):
        result = ""
        for char in s:
            if char != " ":
                result += char 
        return result 
       

#Solution 3
class Solution:
    def removeSpaces(self, s):
        result = []
        for char in s:
            if char != " ":
                result.append(char)
        return "".join(result)