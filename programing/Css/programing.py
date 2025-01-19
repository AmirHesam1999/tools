#!/bin/python3

def clear_commit(name):
    name = name.replace('"', "'")
    return name
import os 
path = input("Please enter new path: ")
os.chdir(path)
os.system("git log")
print("----------------------------")
name = input("Please enter name file : ")
os.mkdir(name)
os.chdir(name)
print("----------------------------")
os.system("touch index.html")
os.system("code index.html")
if input("Please enter (y) for run program in terminal : ") == 'y':
    os.system("google-chrome index.html")
    os.system("git add index.html")
    print("----------------------------")
    n = input("Please enter git commit : ")
    n = clear_commit(n)
    os.system('git commit -m "'+n+'"')
    print("----------------------------")
    os.system("git push")