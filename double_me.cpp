#include <opencv2/opencv.hpp>

using namespace cv;

#ifndef DL_EXPORT  // Windows Oooo Windows, If only you were BSD.
#define DL_EXPORT(kind) kind
#endif

extern "C"{

    extern  DL_EXPORT(void) double_me(void *buffer, const int W, const int H);

     DL_EXPORT(void) double_me(void *buffer, const int W, const int H){
        Mat mat(Size(W, H), CV_32F, buffer);// Wrap with opencv matrix
        mat *= 2 ; // Make an actual inplace action, no need to return a value.
    }

}// Extern
