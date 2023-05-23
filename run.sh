#!/usr/bin/env bash

source ./ShareFiles/env/bin/activate
(cd ./ShareFiles/ && bash runFlask.sh &)
(cd ./Notes && ng serve &)
echo "ng_pid=$ng_pid"
