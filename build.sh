#!/bin/bash


if [ ! -e /usr/bin/python3 ]; then
	echo "Not install python3"
fi

if [ ! -e /usr/bin/pip3 ]; then
	if [ ! -e /usr/local/bin/pip3 ]; then
		echo "Not install pip3"
		python3 get-pip.py		
	fi
fi

version=`python3 --version`
python_version=${version:7:3}
PIP="pip${python_version}"
echo $PIP

$PIP install grequests 
