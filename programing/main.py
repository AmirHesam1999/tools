#!/bin/python3
# get value for edit inner text 
name = input("Enter name: ")

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
print(name)
