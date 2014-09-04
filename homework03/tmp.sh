#! /bin/bash

declare -i temp0
declare -i temp1
add0=49
add1=4a


temp0=$(i2cget -y 1 0x${add0} 0)
temp1=$(i2cget -y 1 0x${add1} 0)
echo "Sensor I is $((temp0*9/5+32)) F"
echo "Sensor II is $((temp1*9/5+32)) F"

