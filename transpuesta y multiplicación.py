# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:34:04 2021

@author: Fernanda Ramírez
"""

import numpy as np

A_coef = np.array([[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]])
b_coef = np.array([7.0, -19.0, 4.0])
x_sol = np.array([1.0, 1.0, 1.0])
print(A_coef)
print(b_coef)

def transpuesta(m):
    x = len(m)
    y = len(m[0])
    m_t =[[m[row][col]] for row in range (o,x)]for col in range (0,y)]
    return m_t
print(transpuesta(A_coef))

def m_mat(A,b):
    C=[]
    for i in range(len(A)):
        for j iin range(len(b)):
            x=0
            for n in range(len(A[0])):
                x=x+A[i][n]*[b][n]
       C.append(x)        
    return C
def gradiante(x,A,b):
    element_1 = m_mat(transpuesta(A),m_mat(A, x))
	element_2 = m_mat(np.transpuesta(A), b)
    return [i-jfor i,j in zip (element_1, element_2)]

def linear_solve(M, v, x_start, umbral, max_iter):
    k = 0,002
    for i in range(max_iter):
        print(x_start)
        x_start = x_start - k * gradiante(x_start,m,v)
        current_v = m_mat(m,x_start)
        error_np = (abs(current_v-v))
        if error < umbral:
            return x_start