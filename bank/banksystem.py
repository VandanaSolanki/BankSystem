# -*- coding: utf-8 -*-
"""BankSystem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-WXK2oGEFFiBXNcXuHauV_jH_AQtww5M

For New User
"""

cust_data = {}
new_user_attributes = ['name', 'address', 'phone num', 'govt id', 'amount']

import random

def new_user():
  acc_num = random.randint(10000,99999)    # Write your code here
  
  new_user_inputs=[]

  for i in range(len(new_user_attributes)):
    user_input = input("Enter " + new_user_attributes[i] + ":\n")
    if new_user_attributes[i] == 'amount':
      new_user_inputs.append(int(user_input))
    else:
      new_user_inputs.append(user_input)

  cust_data[acc_num] = dict(zip(new_user_attributes, new_user_inputs))

  print("Your details are added successfully.\nYour account number is", acc_num) 
  print("Please don't lose it.")

new_user()
cust_data

"""For Existing User"""

def existing_user():
  acc_num =int(input("Enter account number"))   # Write your code here
  while acc_num not in cust_data:
    acc_num = int(input("Not found. Please enter your correct account number:\n"))
    
  print(" Welcome,",cust_data[acc_num]["name"],"\nEnter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount.")

  user_choice = input()
  while user_choice not in ['1','2','3']:
    print("\nInvalid input!")
    print("Enter 1 to check your balance.\nEnter 2 to withdraw an amount.\nEnter 3 to deposit an amount.")
    user_choice = input()
  
  # If 'user_choice == 1' then display the account balance i.e. 'cust_data[acc_num]['amount']'
  if user_choice == '1':
    print(cust_data[acc_num]["amount"])  

  # Else if 'user_choice == 2' then subtract the withdrawal amount from the available balance.
  elif user_choice == '2':
    amt = int(input("\nEnter the amount to be withdrawn:\n"))
    if amt > cust_data[acc_num]['amount']:
      print("\nInsufficient balance.\nAvailable balance:", cust_data[acc_num]['amount'])
    else:
      new_amt = int(cust_data[acc_num]['amount']) - amt
      cust_data[acc_num]['amount'] = new_amt
      print("\nWithdrawal successful.\nAvailable Balance:", cust_data[acc_num]['amount'])

  # Else if 'user_choice == 3' then add the deposit amount to the available balance.
  elif user_choice == '3':
    amt = int(input("\nEnter the amount to be deposited:\n"))
    new_amt = int(cust_data[acc_num]['amount']) + amt
    cust_data[acc_num]['amount'] = new_amt
    print("\nDeposit successful.\nAvailable Balance:", cust_data[acc_num]['amount'])

existing_user()

"""Run as an Application"""

# Create an infinite while loop to run the application.
while True:
    valid_inputs = ['1','2','3']
    print("Welcome to the Bank!")
    print("\nEnter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.") 

    user_choice = input()
    while user_choice not in ['1','2','3']:
        print("Invalid input!")
        print("Enter 1 if you are a new customer.\nEnter 2 if you are an existing customer.\nEnter 3 to terminate the application.\n")
        user_choice = input()

    # If the user enters 1, then call the 'new_user()' function (to create a new account for the user and get their personal details).
    if user_choice == '1':  
        new_user()
        print("Thank you, for banking with us!")

    # Else If the user enters 2, then call the 'existing_user()' function (to check balance, withdraw an amount and to diposite an amount).
    elif user_choice == '2':
        existing_user()
        print("Thank you, for banking with us!")

    # Else If the user enters 3, then terminate the application with the 'Thank you, for banking with us!' message. 
    elif user_choice == '3':
        print("Thank you, for banking with us")
        break