import numpy as np
from ctypes import cdll, c_void_p, c_long
from timeit import default_timer as dt
import matplotlib.pylab as plt

dll_path = 'build/libdouble_me.so.dylib'  # remove .dylib if not OSX
double_me_lib = cdll.LoadLibrary(dll_path)  # Load compiled library.

# Pre allocate a numpy array.
x = np.arange(6).reshape(2, 3)
# Flatten array to C type array.
x = np.ascontiguousarray(x, dtype=np.float32)  # Same as CV_32F

print("Original array:\n", x)


# The C function header is:
# void double_me(void *buffer, const int W, const int H);
# So lets convert the pyth
# Cast to c type pointer and 2 longs W/H.
H, W = c_long(x.shape[0]), c_long(x.shape[1])
P = x.ctypes.data_as(c_void_p)  # The C pointer


# Lets call the in-place C function:
double_me_lib.double_me(P, W, H)

# Operations are in-place, so the result is stored in the original array.
print("Same Array after c code:\n", x)

# Now Let's time it

x = np.random.randn(10000, 10000).astype(np.float32)
start_time = dt()
x = np.ascontiguousarray(x)
print("Flatten took %d ms for %d floats" % ((dt() - start_time) * 1000, x.size))


def numpy_call(x):
    start_time = dt()
    x *= 2.0
    rt = (dt() - start_time) * 1000
    # print("Python numpy took %d ms for %d floats" % (rt, x.size))
    return rt


def opencv_call(x):
    start_time = dt()
    H = c_long(x.shape[0])
    W = c_long(x.shape[1])
    P = x.ctypes.data_as(c_void_p)  # The C pointer
    double_me_lib.double_me(P, W, H)
    rt = (dt() - start_time) * 1000
    # print("OpenCV C code took %d ms for %d floats" % (rt, x.size))
    return rt


rt_numpy = list()
rt_opencv = list()
for i in range(50):
    rt_numpy.append(numpy_call(x))
    x /= 2.0  # Normlize so we dont explode
    rt_opencv.append(opencv_call(x))
    x /= 2.0  # Normlize so we dont explode

rt_numpy_mean = np.mean(rt_numpy[1:])
rt_opencv_mean = np.mean(rt_opencv[1:])

plt.plot(rt_numpy[1:], label='numpy %d ms' % rt_numpy_mean)
plt.plot(rt_opencv[1:], label='CV4 %d ms' % rt_opencv_mean)
plt.legend()
plt.title('Run time (ms) for %d floats' % x.size)
plt.show()
