#!/bin/sh
set -v
./makejson.sh
./states_pct.sh > statepcts.dat
./states_pct_stats.py > report.txt
