#!/bin/bash
vim programing.sh
git add programing.sh
echo "Please enter git commit : "
read com
git commit -m "$com"
git push
