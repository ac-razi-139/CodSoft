# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 21:21:05 2023

@author: hp
"""

class TodoList:
    def __init__(self):
        self.tasks=[]
    def Add_tasks(self,new_task):
        self.new_task=new_task
        self.tasks.append(new_task)
    def Remove_task(self,rem_task):
        self.rem_task=rem_task
        if rem_task in self.tasks:
            self.taks.remove(rem_task)
            print(f"Task {rem_task} removed from the list.")
        else:
            print(f"Task {rem_task} not found in list.")
    def show_tasks(self):
        if self.tasks:
            print(f"Tasks:")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}. {task}")
        else:
            print(f"Task not found.")
def main():
    obj=TodoList()
    while True:
        print(f"1. Add Task")
        print(f"2. Remove Task")
        print(f"3. Show Tasks")
        print(f"4. Exit")
        
        choice=int(input("Enter your choice: "))
        if choice==1:
            new_task=input("Enter the task:")
            obj.Add_tasks(new_task)
        elif choice==2:
            rem_task=input("Enter the task to remove: ")
            obj.Remove_task(rem_task)
        elif choice==3:
            obj.show_tasks()
        elif choice==4:
            print(f"Exit")
            break
        else:
            print(f"Invalid choice.Please select a valid option.")
main()
        
            
            
            
            
            
        