#!/bin/sh
#set -v
for file in json/*.json
do
   ./states_pct.py "$file"
done
