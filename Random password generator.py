# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:14:23 2023

@author: hp
"""

import random
import string
import sys
class RandomPasswordGenerate:
    def length_choice(self):
        self.length=int(input("Enter the desired password length:"))
        if self.length<0:
            print(f"Password length must be greater than 0.")
            sys.exit()
        elif self.length>0:
            return True
        else:
            raise ValueError("Please enter a valid integer for password length.")
    def generate_password(self):
        my_password=[]
        password=string.ascii_letters + string.digits + string.punctuation
        for number in range(self.length):
            my_password.append(random.choice(password))
        password="".join(my_password)
        print("Generated password:",password)
obj=RandomPasswordGenerate()
obj.length_choice()
obj.generate_password()