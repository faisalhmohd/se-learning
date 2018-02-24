#!/bin/bash

read total
SUM=0

for ((i=1; i<=$total; i++))
do
    read tmp
    SUM=$((SUM+tmp))
done

printf "%.3f\n"  $( echo "scale=4; $SUM/$total" | bc -l )