#!/bin/bash

sed 's/\\\\/#/g; s/\\"/#/g; s/\\x[a-f0-9][a-f0-9]/###/g; s/\"/#/g; s/[^#]//g' input.txt | grep -o . | wc -l
#1350

sed 's/\\/#/g; s/"/#/g; s/^/#/g; s/$/#/g; s/[^#]//g' input.txt | grep -o . | wc -l
#2085