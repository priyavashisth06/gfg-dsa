'''
Intersection of Two Sorted Arrays
Difficulty: Easy    Accuracy: 47.82%    Submissions: 14K+    Points: 2    Average Time: 10m

Given two sorted arrays a[] and b[], where each array may contain duplicate elements, return the elements in the intersection of the two arrays in sorted order.

Note: Intersection of two arrays can be defined as the set containing distinct common elements that are present in both of the arrays.

Example 1:
Input: a[] = [1, 1, 2, 2, 2, 4], b[] = [2, 2, 4, 4]
Output: [2, 4]
Explanation: Distinct common elements in both the arrays are: 2 and 4.

Example 2:
Input: a[] = [1, 2], b[] = [3, 4]
Output: []
Explanation: No common elements.

Example 3:
Input: a[] = [1, 2, 3], b[] = [1, 2, 3]
Output: [1, 2, 3]
Explanation: All elements are common.


Constraints:
1 ≤ a.size(), b.size() ≤ 105
-109≤ a[i], b[i] ≤ 109
'''

class Solution:
    def intersection(self, a, b):
        i = j = 0
        rest = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                if not rest or rest[-1] != a[i]:
                    rest.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return rest