#!/bin/bash

OUTPUT_FILE="/opt/stackstorm/output.txt"

execute_with_sudo() {
    local cmd="$1"
    if [ "$(id -u)" != "0" ]; then
        sudo $cmd >> "$OUTPUT_FILE" 2>&1
    else
        $cmd >> "$OUTPUT_FILE" 2>&1
    fi
}

{
    echo "date: $(date)" >> "$OUTPUT_FILE"
    echo "uname: $(uname -a | awk '{print $2}')" >> "$OUTPUT_FILE"
    echo "uptime: $(uptime | awk -F "up |, | users" '{print $2}')" >> "$OUTPUT_FILE"

    top_output=$(top -b -n 1 -o %CPU)
    echo "Load Average: $(echo "$top_output" | grep -E 'load average:' | awk '{print $10, $11, $12}')" >> "$OUTPUT_FILE"
    echo "Process ID: $(echo "$top_output" | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1}')" >> "$OUTPUT_FILE"
    echo "User/Owner: $(echo "$top_output" | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1}')" >> "$OUTPUT_FILE"
    echo "CPU Utilization: $(echo "$top_output" | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1}')" >> "$OUTPUT_FILE"
    echo "Command/Application: $(echo "$top_output" | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1}')" >> "$OUTPUT_FILE"
} 2>&1

exit 0