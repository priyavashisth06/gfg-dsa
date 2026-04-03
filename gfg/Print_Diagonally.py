'''Print Diagonally


Difficulty: Easy 
Accuracy: 66.11% 
Submissions: 48K+ 
Points: 2 
Average Time: 10m


Give a n * n square matrix mat[][], return all the elements of its anti-diagonals from top to bottom.

Example 1:

Input: n = 2, mat[][] = [[1, 2],
                        [3, 4]]
Output: [1, 2, 3, 4]
Explanation: 
https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/705888/Web/Other/blobid1_1774682773.png


Example 2:

Input: n = 3, mat[][] = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]
Explanation: 
https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/705888/Web/Other/blobid0_1774682722.png

Constraints:
1 ≤ n ≤ 103
0 ≤ mat[i][j] ≤ 106'''


class Solution:
    def diagView(self, mat):
        n=len(mat);res=[]
        for c in range(n):
            i,j=0,c
            while i<n and j>=0:
                res.append(mat[i][j]);i+=1;j-=1
        for r in range(1,n):
            i,j=r,n-1
            while i<n and j>=0:
                res.append(mat[i][j]);i+=1;j-=1
        return res