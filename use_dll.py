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


