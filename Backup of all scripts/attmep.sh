#!/bin/bash

var=$(date +"%Y-%m-%d_%H-%M-%S")
filename="$var.txt"

# Start candump in the background, redirecting its output to both the file and awk
candump can0 | awk -v filename="$filename" '{ timestamp=strftime("%Y-%m-%d %H:%M:%S"); print timestamp " " $0; fflush(); print timestamp, $0 >> filename }' &
candump_pid=$!

# Trap to stop candump and terminate the script gracefully
trap 'kill $candump_pid; exit' INT TERM EXIT

# Keep the script running
wait $candump_pid
