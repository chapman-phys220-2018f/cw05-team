#!/bin/bash

if [ -e fibs.csv ]
then
    if [ -e fibs.csv.bak ]
    then
        echo "fibs.csv.bak already exists"
        exit 1
    else
        mv fibs.csv fibs.csv.bak
        echo "Backing up fibs.csv to fibs.csv.bak, overwriting fibs.csv"
    fi
fi
     
for i in $(seq 10000); do
    ./fib.py ${i} >> fibs.csv
done
sed -i ':a;N;$!ba;s/\n/, /g' fibs.csv
