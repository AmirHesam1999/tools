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
os.system("touch Main.java")
os.system("code Main.java")
if input("Please enter (y) for run program in terminal : ") == 'y':
    os.system("java Main.java")
    os.system("git add Main.java")
    print("----------------------------")
    n = input("Please enter git commit : ")
    n = clear_commit(n)
    os.system('git commit -m "'+n+'"')
    print("----------------------------")
    os.system("git log")
    if input("Are you push git? (y/n): ") == 'y':
        os.system("git push")