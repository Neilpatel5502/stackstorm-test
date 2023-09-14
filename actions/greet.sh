#!/bin/bash

# Run the commands and capture their output
output=$(date)
output="$output\n$(uname -a | awk '{print $2}')"
output="$output\n$(uptime | awk -F 'up |, | users' '{print $2}')"
output="$output\n$(top -b -n 1 -o %CPU | grep -E 'load average:' | awk '{print $10, $11, $12}')"
output="$output\n$(top -b -n 1 -o %CPU | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1, $2, $9, $12}')"

echo -e "$output"