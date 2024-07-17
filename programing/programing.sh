#!/bin/bash
cd /home/hesam/Documents/Hesam/Css/tutorial/text/Shadow
echo "Please enter name file : "
read name
mkdir $name
touch $name/index.html
code $name/index.html
read stop
google-chrome $name/index.html
git add $name/index.html
echo "Please enter git commit : "
read com
git commit -m "$com"
git push
 

