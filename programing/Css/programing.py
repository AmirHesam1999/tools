#!/bin/python3
def clear_name (name):
    # replace value " " to "_"
    name = name.replace(" ", "_")

    name = name.replace("/", "_or_")

    # if text has "|" before "|" add "\"
    i = 0
    i = name .rfind("|")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 

    i = 0
    i = name .rfind("(")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 

    i = 0
    i = name .rfind(")")
    if i != -1:
        name = name[:i]+ '\\' + name[i:] 
    return name
def clear_commit(name):
    name = name.replace('"', "'")
    return name
import os 
path = input("Please enter new path: ")
os.chdir(path)
print("----------------------------")
name = input("Please enter name file : ")
name = clear_name(name)
s = "mkdir "+name
print("----------------------------")
os.system("mkdir "+name)
os.chdir(name)
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
    os.system("git log")
    if input("Are you push git? (y/n): ") == 'y':
        os.system("git push")