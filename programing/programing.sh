#!/bin/bash
echo "Please enter new path : "
read path
cd $path
echo "-----------------------------------------------"
echo "Please enter name file : "
read name
echo "-----------------------------------------------"
mkdir $name
touch $name/index.html
code $name/index.html
read stop
google-chrome $name/index.html
echo "-----------------------------------------------"
git add $name/index.html
echo "Please enter git commit : "
read com
echo "-----------------------------------------------"
git commit -m "$com"
echo "-----------------------------------------------"
git push
 

