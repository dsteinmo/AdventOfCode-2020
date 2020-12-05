#!/bin/bash
# Replace newlines with ", " for copy+paste into python array. 
sed -z "s/\n/, /g" day1_input.txt > day1_input_1line.txt