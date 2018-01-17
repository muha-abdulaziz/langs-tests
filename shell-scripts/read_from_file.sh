#!/usr/bin/bash

exec 4< names.list

while true
    do
        read -u 4 line
        if [ $? -eq 1 ]
        then
            break
        fi
        echo "Hello $line"
    done
