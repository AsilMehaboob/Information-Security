#!/bin/bash

echo "Enter username:"
read username

while true
do 
    if who | grep -w "$username" > /dev/null
    then
        echo "User $username is logged in."
    else
        echo "User $username is not logged in, Checking again in 30 seconds..."
    fi
    sleep 30
done