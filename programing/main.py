#!/bin/python3
name = input("Enter name: ")
i = 0
i = name .rfind("_")
if  i != -1:
    name = name.replace(" ", "_")
i = 0
i = name .rfind("/")
if i != -1:
    name = name.replace("/", "_or_")
i = 0
i = name .rfind("|")
if i != -1:
    name = name[:i]+ '\\' + name[i:] 
print(name)
