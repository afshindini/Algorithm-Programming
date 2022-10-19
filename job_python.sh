#!/bin/bash -l 

for file in `ls $problem/*.py`; do
    if [[ ${file} != *"test"* ]]; then
        pytype ./$file
        mypy ./$file
    else
        echo "Run test file for $file"
        python ./$file
    fi
done

i=0
for file in `ls $problem/*.py`; do
    if [[ ${file} != *"test"* ]]; then
        i=$((i+1))
        echo "Run $problem$i.py file"
        python ./$file
    fi
done