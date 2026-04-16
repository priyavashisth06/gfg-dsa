'''
Implement Atoi
Difficulty: Medium    Accuracy: 32.58%    Submissions: 307K+    Points: 4    Average Time: 15m

Given a string s, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.

The conversion follows these rules:
1. Ignore Leading Whitespaces: Skip all leading whitespace characters.
2. Check Sign: If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.
3. Read Digits: Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.
4. Handle Overflow: If the number exceeds the range of a 32-bit signed integer:
   - Return 2³¹ - 1 (i.e., 2147483647) if it is greater than the maximum value.
   - Return -2³¹ (i.e., -2147483648) if it is smaller than the minimum value.
Return the final integer value.



Example 1:
Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer



Example 2:
Input: s = " -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.



Example 3:
Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 2³¹ - 1, therefore print 2³¹ - 1 = 2147483647.



Example 4:
Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -2³¹, therefore print -2³¹ = -2147483648.



Example 5:
Input: s = "  -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character 'g' was encountered.


Constraints:
1 ≤ |s| ≤ 15
'''



class Solution:
    def myAtoi(self, s): 
        i, n = 0, len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = -1 if i < n and s[i] == '-' else 1
        if i < n and s[i] in '+-':
            i += 1
        
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        
        return max(-2**31, min(2**31 - 1, num))