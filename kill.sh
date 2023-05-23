#!/bin/bash
# This script finds and kills the process running on port 4000

# Find the PID of the process running on port 4000
PID=$(sudo lsof -t -i:4200)

# Check if a PID was found
if [ -z "$PID" ]
then
    echo "No process found running on port 4000"
else
    # Kill the process
    kill $PID
    echo "Process $PID running on port 4000 terminated"
fi

#!/bin/bash
# This script finds and kills the process running on port 4000

# Find the PID of the process running on port 4000
PID=$(sudo lsof -t -i:5000)

# Check if a PID was found
if [ -z "$PID" ]
then
    echo "No process found running on port 4000"
else
    # Kill the process
    kill $PID
    echo "Process $PID running on port 4000 terminated"
fi
