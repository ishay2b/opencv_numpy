import numpy as np
import ctypes

dll_path = 'build/libdouble_me.so.dylib'  # remove .dylib if not OSX
double_me_lib = ctypes.cdll.LoadLibrary(dll_path)  # Load compiled library.

# Pre allocate a numpy array.
my_array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)  # Same as CV_32F

# Flatten array to C type array.
my_array = np.ascontiguousarray(my_array)

print("Original array:\n", my_array)

# Cast to c type pointer and 2 longs W/H and call C code.
double_me_lib.double_me(my_array.ctypes.data_as(ctypes.c_void_p), ctypes.c_long(2), ctypes.c_long(3))

# Operations are inplace there for we can see the result in same array.
print("Same Array after c code:\n", my_array)


