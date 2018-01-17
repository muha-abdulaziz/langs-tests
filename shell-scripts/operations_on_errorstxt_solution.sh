#!/usr/bin/bash

# \ua0 is the non breaking space
for i in `cat errors.txt | cut -f 1 -d $'\ua0' | sort -u`
do
    NU=`cat errors.txt |grep "^${i}" | sort -u | wc -l`
    echo "Error Code $i has $NU different descriptions" 
done
