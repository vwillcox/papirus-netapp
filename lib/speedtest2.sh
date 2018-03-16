#!/bin/bash


OUTPUT=`cat /home/pi/papirus-netapp/files/speedtest.txt`
DOWNLOAD=`echo "$OUTPUT" | grep Download | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`
UPLOAD=`echo "$OUTPUT" | grep Upload | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`
#TIME=`echo "$OUTPUT" | grep at | sed 's/[a-zA-Z:]* \([0-9]*\.[0-9]*\) [a-zA-Z/]*/\1/'`

echo "$DOWNLOAD" > /home/pi/papirus-netapp/files/graph.txt
echo "$UPLOAD" > /home/pi/papirus-netapp/files/graph2.txt
#echo "up.value $UPLOAD"
