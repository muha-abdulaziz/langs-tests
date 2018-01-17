#!/usr/bin/bash

########################################################################
## preparing

# check if the file errors.txt is exist
if [ ! -f errors.txt ]
then
    echo "the file 'errors.txt' doesnot exist"
    exit 1
else
    # check if current place not writeable
    if [ -O $PWD ]
    then
        ERRORS="errors.txt.sorted"
        ERRORS_ID="errors_id"
        ERRORS_STR="errors_str"
    else
        TMP="/tmp"
        ERRORS="$TMP/errors.txt.sorted"
        ERRORS_ID="$TMP/errors_id"
        ERRORS_STR="$TMP/errors_str"
    fi


    # sort errors.txt file and put th output in errors.txt.sorted file
    sort -k 1 errors.txt > $ERRORS
    

    # slice each line in the file errors.txt.sorted
    # and put the errors id in errors_id file
    # and the error description in errors_str
    cut -c 1-6 errors.txt.sorted > $ERRORS_ID
    cut -c 8- errors.txt.sorted > $ERRORS_STR
fi

########################################################################
## The start of the script 


# put errors_id in std file number 4
exec 4< $ERRORS_ID
# put errors_str in std file number 5
exec 5< $ERRORS_STR

OLD_L1=""
OLD_L2=""
OK=0
COUNT=0
DUP=0
while true
    do
        # read error_id file
        read -u 4 LINE1
        # read error_str file
        read -u 5 LINE2
        
        # if reach the end of file exit
        if [ $? -eq 1 ]
        then
            echo "$COUNT lines has the same error id but not the same description."
            echo "$DUP Duplict lines"
            break
        fi
        #echo "$line1  $line2"

        if [ -z $OLD_L1 ] && [ -z $OLD_L2 ]
        then
            OLD_L1=$LINE1
            OLD_L2=$LINE2
            
        # just skip this line
        elif [ $OK -eq 1 ]
        then
            OK=0

        elif [ "$OLD_L1" == "$LINE1" ]
        then
            DUP=$(( $DUP + 1 ))
            # check if 2 lines have the same id error
            # and diffrente descriptions
            # if they are not the same print both to the STDIN
            if [ "$OLD_L2" != "$LINE2" ]
            then
                OK=1
                COUNT=$(($COUNT + 1))
                #echo "$OLD_L1 $OLD_L2"
                #echo "$LINE1 $LINE2"
                #echo
            
            fi
        fi
        OLD_L1=$LINE1
        OLD_L2=$LINE2
    done

rm $ERRORS_ID $ERRORS_STR $ERRORS
exit 0
