#!/bin/bash

echo "PATH: $PATH"
export PATH=/usr/bin/sar:$PATH
env
sar -u 5 5