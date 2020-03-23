#!/bin/sh
set -v
rm json/*.json
rmdir json
mkdir json
for file in txt/*.txt
do
   ./txt2json.py "$file"
done
mv *.json json
