#!/bin/bash
# Replace newlines with '", "'  for copy+paste into python array. 
sed -z 's/\n/", "/g' day5_input.txt > day5_input_1line.txt