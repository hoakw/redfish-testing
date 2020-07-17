#!/bin/bash

pip3.5 install grequests

python3 redfishMockupServer.py -D ./test &

echo "TEST Start - Get Data"

curl http://localhost:8000/redfish/v1
