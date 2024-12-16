#!/bin/python3
name = input("Enter name: ")
name = name.replace(" ", "_")
name = name.replace("/", "_or_")
print(name)
