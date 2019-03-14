# Using Open CV C/C++ code in C code context on numpy python arrays:

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

```
cd build
cmake ..
make
```

A new shared library named double_me.so is created in the build folder.
Notice OSX adds .dylib extension.

## Now let’s use it from Python:
```
cd ..
python use_dll.py
```


## Result
```
Original array:
 [[1. 2. 3.]
 [4. 5. 6.]]
Same Array after c code:
 [[ 2.  4.  6.]
 [ 8. 10. 12.]]
```

## Main python function

```python
import numpy as np
from ctypes import cdll, c_void_p, c_long

dll_path = 'build/libdouble_me.so.dylib'  # remove .dylib if not OSX
double_me_lib = cdll.LoadLibrary(dll_path)  # Load compiled library.

# Pre allocate a numpy array.
my_array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)  # Same as CV_32F

# Flatten array to C type array.
my_array = np.ascontiguousarray(my_array)

print("Original array:\n", my_array)


# Cast to c type pointer and 2 longs W/H.
H = c_long(my_array.shape[0])
W = c_long(my_array.shape[1])
P = my_array.ctypes.data_as(c_void_p)  # The C pointer

# The C function header is:
# void double_me(void *buffer, const int W, const int H);

# Lets call the inplace C function:
double_me_lib.double_me(P, W, H)

# Operations are inplace there for we can see the result in same array.
print("Same Array after c code:\n", my_array)

```

## Main C code
```C
DL_EXPORT(void) double_me(void *buffer, const int W, const int H){
    Mat mat(Size(W, H), CV_32F, buffer);// Wrap with opencv matrix. Notice assume np.float32. watch out, no type checks.
    mat *= 2 ; // Make an actual inplace action, no need to return a value.
}
```
