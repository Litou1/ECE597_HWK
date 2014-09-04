#!/bin/bash
# Set up gpio 7 2 to read and gpio 3 15 to write
cd /sys/class/gpio

echo 7 > export
echo 2 > export

echo 3 > export
echo 15 > export

echo in  > gpio7/direction
echo in  > gpio2/direction

echo out > gpio3/direction
echo out > gpio15/direction