#!/bin/bash



file=`$(echo $1)`

if [ $file==1 ]
then
	echo "Welcome"

elif [ $file==0 ]
then
	echo "No"
else
	echo "what"

fi
