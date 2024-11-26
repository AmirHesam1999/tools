#!/bin/bash
echo "Please enter new path : "
read path
cd $path
echo "-----------------------------------------------"
git add Main.java
echo "Please enter git commit : "
read com
echo "-----------------------------------------------"
git commit -m "$com"
echo "-----------------------------------------------"
git push

