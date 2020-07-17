#!/bin/bash

./up_server.sh &

sleep 4

echo "TEST Start - Get Data"

curl http://localhost:8000/redfish/v1



echo "TEST Finish!!!"

kill -9 $(ps -ef | grep redfishMockup | awk '{ print $2 }')
