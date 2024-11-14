#!/bin/bash
echo "Please enter new path : "
read path
cd $path
echo "-----------------------------------------------"
echo "Please enter name file : "
read name
echo "-----------------------------------------------"
mkdir $name
touch $name/Main.java
code $name/Main.java
echo "Please enter for run program in terminal : "
read stop
java $name/Main.java
echo "-----------------------------------------------"
git add $name/Main.java
echo "Please enter git commit : "
read com
echo "-----------------------------------------------"
git commit -m "$com"
echo "-----------------------------------------------"
git push
 

