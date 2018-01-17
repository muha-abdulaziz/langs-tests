#!/usr/bin/bash

MYNAME=" "
#until [ -z "$MYNAME" ]
#until false
while [ -n $MYNAME ]
    do
	    echo "What is your name?"
	    read MYNAME
	    if [ -z "$MYNAME" ]
	    then
            echo "You entered nothing."
            echo "bye!"
           exit	
        fi
        echo "your name is ${MYNAME}."
    done
