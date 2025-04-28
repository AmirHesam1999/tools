#!/bin/python3
import os 
def program(b):
    if b:
        name = input("Please enter name file : ")
        os.mkdir(name)
        os.chdir(name)
        print("----------------------------")
        os.system("touch main.py")
        os.system("code main.py")
    else:
        os.system("code index.html")
        programptwo()

def programptwo():
    if input("Please enter (y) for run program in terminal : ") == 'y':
        os.system("google-chrome index.html")
        n = input("Are you complete program (y/n) : ")
        if n == 'y':
            os.system("git add main.py")
            print("----------------------------")
            n = input("Please enter git commit : ")
            n = clear_commit(n)
            os.system('git commit -m "'+n+'"')
            print("----------------------------")
            os.system("git push")
        elif n == "n":
            program(False)

def clear_commit(name):
    name = name.replace('"', "'")
    return name

path = input("Please enter new path: ")
os.chdir(path)
os.system("git log")
print("----------------------------")
program(True)
programptwo()