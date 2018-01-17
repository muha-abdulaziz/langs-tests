#!/usr/bin/bash

NUM=$((0))
while [ $NUM -lt $((101)) ]
    do
        echo $NUM
        #NUM=$((NUM + 1))
        NUM=$((NUM++))
    done
