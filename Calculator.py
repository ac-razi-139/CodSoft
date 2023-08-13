# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:47:33 2023

@author: hp
"""

class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Addition(self):
        addition_result=self.x+self.y
        print(f"Addition result is: {addition_result}")
    def Subtraction(self):
        subtraction_result=self.x-self.y
        print(f"Subtraction result is: {subtraction_result}")
    def Multiplication(self):
        multiplication_result=self.x*self.y
        print(f"Multiplication result is: {multiplication_result}")
    def Division(self):
        if self.y<0:
            raise ValueError("zero division error.")
        else:
            division_result=self.x/self.y
            print(f"Division result is: {division_result}")  
obj=Calculator(2,3)
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()
            
              
        
        