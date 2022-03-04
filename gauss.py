#!/usr/bin/env python3
"""Naive implementation of Gauss's Method."""
# 2022-Mar-01 JH GPL
#literally ctr+c and ctr+v
A = [[1, 2, 3, 4],
     [3, 0, 2, 1],
     [2,-1, 5, 1]]
num_rows = len(A)
num_cols = len(A[0])
for k in range(0, num_rows-1):  # row being used
    # print("A=", A)
    # print("row being used k=",k)
    for i in range(k+1, num_rows):  # row being changed
        # print("  row being changed i=",i)
        pivot_mult = A[i][k]/A[k][k]
        # print("  pivot_mult=",pivot_mult)
        for j in range(0, num_cols):  # column number in that row
            # print("    column number j=",j)
            # print("      change entry by ",- pivot_mult*A[k][j])
            A[i][j] =  A[i][j] - pivot_mult*A[k][j]
print("solution is: ",A)