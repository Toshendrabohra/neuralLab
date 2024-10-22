#!/bin/bash

# Check arguments 
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <min> <max>"
  exit 1
fi

# Get min and max values
min=$1
max=$2


for i in $(seq $min $max); do
  # Create directory
  mkdir -p "step-$i"

  # Write data to the data.json file
  echo -e "\"step-$i\"" > "step-$i/data.json"
  
  echo "Created directory step-$i with data.json"
done
