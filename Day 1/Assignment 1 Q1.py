# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:06:22 2021

@author: Win 7
"""

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/ : ")

sol = 0
if ch == '+':
    sol = num1 + num2
elif ch == '-':
    sol = num1 - num2
elif ch == '*':
    sol = num1 * num2
elif ch == '/':
    sol = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", sol)