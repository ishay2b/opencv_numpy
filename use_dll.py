import numpy as np
import ctypes

dll_path = 'build/libdouble_me.so.dylib'
double_me_lib = ctypes.cdll.LoadLibrary(dll_path)

# void double_me(unsigned char *buffer, const int W, const int H);

my_array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
my_array = np.ascontiguousarray(my_array)  # Flatten array to C type array.
double_me_lib.double_me(my_array.ctypes.data_as(ctypes.c_void_p), ctypes.c_long(2), ctypes.c_long(3))
print(my_array)


