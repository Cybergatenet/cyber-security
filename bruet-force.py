from random import *
import os


u_pwd = input("Enter a Password: ")
pwd = ['a', 'b', '0', '1','2', '3', '4']

pw = ""
while(pw != u_pwd):
    pw = ""
    for letter in range(len(u_pwd)):
        # guess_pwd = pwd[randint(0,6)]
        guess_pwd = pwd[randint(0,6)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cracking Password... Please wait...")
        os.system("cls")
print(f"Your Password is : {pw}")

# os.system("start calc.exe")

# IaaS - infrastructure As A Service
# PaaS - P
# SAAS - 