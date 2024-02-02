#!/usr/bin/bash


while :
do
  cansend can0 0C1#C8.00.01.00.00.99
  sleep 4
  echo "hello"
done

