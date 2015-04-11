#!/bin/bash

# connects slicer and foodfindserver

python ./FoodFindServer/server.py &
PID=$!

trap "killall $PID" SIGTERM SIGINT

while 1; do
    sleep 5
    if [ -e "test.jpg" ]
    then
        echo "Exists..."
        sleep 5 # make sure it finished transferring
        python ./ProofOfConcept/Tester.py ./ProofOfConcept/MMAPIK.txt test.jpg
        rm test.jpg
    fi
done
