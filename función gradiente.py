# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:40:49 2021

@author: diana
"""

import numpy as np

A_coef = np.array([[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]])
b_coef = np.array([7.0, -19.0, 4.0])

x_sol = np.array([1.0, 1.0, 1.0])


def gradient(x, A, b):
	element_1 = np.dot(np.transpose(A),np.dot(A, x))
	element_2 = np.dot(np.transpose(A), b)
	return element_1 - element_2

    
def linear_solve(A, b, x_start, umbral, max_iter):
    k = 0.002
    for i in range(max_iter):
        x_start = x_start - k * gradient(x_start, A, b)
        current_b = np.dot(A,x_start)
        error_np = np.sum(np.abs(current_b-b))
        if error_np < umbral:
            return x_start

print(linear_solve(A_coef, b_coef, x_sol, 0.00001, 10000))
