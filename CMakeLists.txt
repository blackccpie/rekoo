cmake_minimum_required(VERSION 3.5)

project (rekoo)

include_directories(
    .
    "${CMAKE_SOURCE_DIR}/../DeepBeliefSDK/RaspberryPiLibrary"
)

link_directories("${CMAKE_SOURCE_DIR}/../DeepBeliefSDK/RaspberryPiLibrary")

add_executable(rekoo main.c)

target_link_libraries(rekoo
jpcnn
)
