#!/bin/bash

# - Place the input (e.g., 3113322113) in the file "i" before executing the script.
# - Call the script:
#   $ ./day10_extremelyShort.sh 40

seq -f "fold -w1 i|uniq -c|tr -d '\n '>t;cat t>i" $1|sh;wc -c i




