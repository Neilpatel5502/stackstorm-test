#!/bin/bash

# Run the commands and capture their output
output=$(date)
output="$output\n$(uname -a | awk '{print $2}')"
output="$output\n$(uptime | awk -F 'up |, | users' '{print $2}')"
output="$output\n$(top -b -n 1 -o %CPU | grep -oP 'load average: \K.*$')"
output="$output\n$(top -b -n 1 -o %CPU | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1, $2, $9, $12}')"
output="$output\n$(sar -u 5 5 | grep -E "Average:" | awk '{print $8}')"
output="$output\n$(sar -r 5 5 | grep -E "Average:" | awk '{print $5}')"

output="$output\n$(sar -S 5 5 | grep -E "Average:" | awk '{print $4}')"

output="$output\n$(sar -q 5 5 | grep -E "Average:" | awk '{print $2, $3, $4, $5, $6}')"

echo -e "$output"