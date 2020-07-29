#/bin/bash
./up_server.sh &

sleep 1

echo "Hi there!!"
python3 test_start.py  --host=localhost --port=8000 --dir=./test --time=0.5

kill -9 $(ps -ef | grep redfishMockup | awk '{ print $2 }')
