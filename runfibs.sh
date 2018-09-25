#!/bin/bash
if [ -e fibs.csv.bak ]; then
	echo backup already exists
    exit 1
fi
if [ -e fibs.csv ]; then
    mv fibs.csv fibs.csv.bak
    echo backup file fibs.csv.bak has been created
fi
for i in $(seq 10000); do
   ./fib.py $i >> fibs.csv
done
sed -i ':a;N;$!ba;s/\n/, /g' fibs.csv
