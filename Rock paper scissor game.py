# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 08:22:13 2023

@author: hp
"""
import random
class RockScissorPaper:
    def user_choice(self):
        self.user_input=input("Enter your choice(rock,paper,scissor):").lower()
    def computer_choice(self,my_list):
        self.comp_choice=random.choice(my_list)
    def play_game(self):
        if self.user_choice==self.comp_choice:
            print(f"It's tie.")
        elif (self.user_choice=='rock' and self.comp_choice=="paper") or\
             (self.user_choice=="paper" and self.comp_choice=='scissor') or\
             (self.user_choice=='scissor' and self.comp_choice=='rock'):
             print(f"Computer win.")
        else:
            print(f"You lost the game.")
def main():
    
    obj=RockScissorPaper()
    level=0
    while level<5:
        print(f"\nLevel: {level}")
        obj.user_choice()
        print("User choice:",obj.user_input)
        obj.computer_choice(['rock','paper','scissor'])
        print("Computer choice:",obj.comp_choice)
        obj.play_game()
        level=level+1
main()   
        