# Calling C/C++ code from python:

## This is an example showcasing:
1. Python allocating numpy array.
2. Python calls C code to operate on the array.
3. C code wraps the array as an OpenCV Matrix, and operates on the array (here it multiples by 2).
4. Since the operation is in place and operated on the python allocated array, python code gets the alg result. e.g. The same array multiplied by 2.

## Why like this?
1. No need for python/numpy binding and coding on the C code side.
2. Therefor no code changes to algorithms already written in C code.
3. Easiest way to test existing algorithms written in C using python.
4. No need to allocate memory on C code since allocations are all ready done on python side.
5. Once the python numpy array is contiguous, no overhead to C calls.
6. Operating on OpenCV matrix is a fast way to get built in optimized vector operations.


## What is the nearest alternative?
The other second “best” option is to add C code python bindings, wrap and unwrap objects, handle memory allocations and deallocations. Curiues minds can find more details in the python official example: https://docs.python.org/3/extending/extending.html


## Can I see this magic in action?
Sure, here is how, first let's compile the C code into a shared object.

cd build
cmake ..
make

## Now let’s use it from
cd ..
python use_dll.py
