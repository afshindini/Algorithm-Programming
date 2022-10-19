# Algorithm Programing
In this repository, some the algorithm problems from various resources have been solved.

## Run Python
Most of the codes are developed in python. In order to run each solution, you should define an environmental variable as `problem` and then run the `job_python.sh`. The `job_python.sh` runs the `pytype` and `mypy` in order to check the python code from stylic point of view and then executes all the codes in the related folder.
```shell
chmod u+x job_python.sh
problem=INSERT PROBLEM NAME ./job_python.sh
```