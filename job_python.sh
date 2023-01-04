#!/bin/bash -l 

for file in `ls $problem/*.py`; do
    pytype ./$file
    mypy --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs ./$file
    pylint ./$file
    if [[ ${file} == *"test"* ]]; then
        echo "Run test file for $file"
        pytest ./$file
    fi
done

i=0
for file in `ls $problem/*.py`; do
    if [[ ${file} != *"test"* ]]; then
        echo "Run $file.py file"
        python ./$file
    fi
done