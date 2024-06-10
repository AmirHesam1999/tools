#!/bin/bash
cd /home/hesam/Documents/Hesam/Css/tutorial/Borders/Sides
echo "Please enter name file : "
read name
mkdir $name
touch $name/index.html
code $name/index.html
read stop
google-chrome $name/index.html
git add $name/index.html
echo "Please enter git commit : "
read comm
git commit -m "$comm"
git push
killall code

