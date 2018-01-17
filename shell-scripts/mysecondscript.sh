#!/usr/bin/bash

for i in 1 2 3 4 5 6 7 8 9 0
	do
		echo "What is your name?"
		read MYNAME
                # check if MYNAME is empty or not
                # if it is empty exit
		if [ -z "$MYNAME" ]
	        then
                    echo "You entered nothing."
                    echo "bye!"
		    exit	
                fi
	echo "your name is ${MYNAME}."
	done
