#!/bin/bash


echo "Push file in github"
git config --global user.email "hoakw12@gmail.com"
git config --global user.name "hoakw"
git add * 
git status
git commit -m "$1"
git push -u origin master


echo "Start Jenkins Testing"
curl -X post http://admin:11b606029031ce2ee751e13d9132d743b6@10.0.6.13:8080/job/redfish_build_test/build?token=11b606029031ce2ee751e13d9132d743b6
