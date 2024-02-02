#!/bin/bash

var=$(date +"%Y-%m-%d_%H-%M-%S")

filename="$var.txt"

candump can0 > "$filename.txt" | awk -v filename="$filename" 'BEGIN { while (1) { "date +\"%Y-%m-%d %H:%M:%S\"" | getline timestamp; print timestamp ": " $0 >> filename; close(filename); system("sleep 1"); } }' &
