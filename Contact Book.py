# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:42:01 2023

@author: hp
"""

class Contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
class ContactBook:
    def __init__(self):
        self.contacts=[]
    def add_contacts(self,new_contact):
        self.contacts.append(new_contact)
    def view_contacts(self):
        for my_contact in self.contacts:
            print(f"{my_contact.name} - {my_contact.phone}")         
    def search_contacts(self,search_term):
        my_search=[]
        for numbers in self.contacts:
            if search_term in numbers.name or search_term in numbers.phone:
                my_search.append(numbers)
        return my_search
    def update_contacts(self,index,up_contact):
        self.contacts[index]=up_contact
    def delete_contacts(self,index):
        del self.contacts[index]
def GraphicalUserInterface():
    contact_book=ContactBook()
    while True:
        print(f"Contact Book")
        print(f"1. Add Contact")
        print(f"2. View Contact List")
        print(f"3. Search Contact")
        print(f"4. Update Contact")
        print(f"5. Delete Contact")
        print(f"5. Exit")
        choice=int(input("Select an option."))
        if choice==1:
            name=input("Name: ")
            phone=int(input("Phone Numbe: "))
            email=input("Email: ")
            address=input("Address: ")
            new_contact=Contact(name,phone,email,address)
            contact_book.add_contacts(new_contact)
            print(f"Contact added successfully.")
        elif choice==2:
            print(f"\nContact List:")
            contact_book.view_contacts()
        elif choice==3:   
            search_term=input("Enter name or phone number to search: ")
            search_result =contact_book.search_contacts(search_term)
            if search_result:
                print("\nSearch Results:")
                for contacts in search_result:
                    print(f"{contacts.name} - {contacts.name}")                
            else:
                print("No matching contacts found.")         
        elif choice==4:
            index=int(input("Enter the index of the contact to update: "))
            if 0<=index<=len(contact_book.contacts)-1:
                name=input("Name: ")
                phone=int(input("Phone Numbe: "))
                email=input("Email: ")
                address=input("Address: ")
                up_contact=Contact(name,phone,email,address)
                contact_book.update_contacts(index, up_contact)
                print(f"Contact updated successfully.")
            else:
                print("Invalid syntax.")
        elif choice==5:
            index=int(input("Enter the index of the contact to delete: "))
            if 0<= index <=len(contact_book.contacts):
                contact_book.delete_contacts(index)
            else:
                print(f"Invalid Synatx.")
        elif choice==6:
            print(f"Exiting Contact Book.")
            break
        else:
            print(f"Invalid choice. Please select a valid option.")
            break
GraphicalUserInterface()                
            
            
        
            
            
        