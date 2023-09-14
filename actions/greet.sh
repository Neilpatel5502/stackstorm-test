#!/bin/bash

date
uname -a | awk '{print $2}'
uptime | awk -F "up |, | users" '{print $2}'

top -b -n 1 -o %CPU | grep -E "load average:" | awk '{print $8, $9, $10, $11, $12}'
top -b -n 1 -o %CPU | grep -E '^\s*[0-9]+' | head -n 1 | awk '{print $1, $2, $9, $12}'