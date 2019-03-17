cmake_minimum_required(VERSION 3.5)
project(opencv_numpy)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++1y -pthread -Wall -fpermissive -Wno-write-strings")

set(CMAKE_CXX_STANDARD 14)
find_package(OpenCV REQUIRED)

include_directories( ${OpenCV_INCLUDE_DIRS})
file(GLOB SOURCES
    *.h
    *.hpp
    *.cpp
)

ADD_LIBRARY(double_me.so SHARED ${SOURCES})
target_link_libraries(double_me.so ${OpenCV_LIBS})
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")
