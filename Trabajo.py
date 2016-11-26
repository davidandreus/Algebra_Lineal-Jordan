#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
#import numpy as np

print("Forma Canónica de Jordan")

# Ingreso de la Matriz
matriz = input("Matriz : ")

M = Matrix(matriz) # Convierte los datos a una Matriz

lamda = symbols('λ') # Determina el Simbolo Lambda
p = M.charpoly(lamda) # Calcula el polinomio Característico
#print(factor(p))
print("\nPolinomio Característico")
print(p) # Muestra el Polinomio Característico

# Calcula los Valores Propios
print("\nValores Propios")
print(factor(p))
print(M.eigenvals())

# Determina si la Matriz es Diagonalizable
print("\n¿Es Diagonalizable la Matriz?")
diagonal = M.is_diagonalizable()
print(diagonal)

if diagonal == True:
	X, H = M.diagonalize()
	print("P y P^-1")
	print(X)
	print(X.inv())
	print("Matriz Diagonalizable")
	print(H)
else:
	print("Vector Generalizado")
	(V, J) = M.jordan_form()
	print(V)
	print("Jordan")
	print(J)
