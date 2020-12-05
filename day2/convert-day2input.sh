#!/bin/bash
# Replace newlines with '", "'  for copy+paste into python array. 
sed -z 's/\n/", "/g' day2_input.txt > day2_input_1line.txt