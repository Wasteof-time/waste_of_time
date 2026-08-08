cmake_minimum_required(VERSION 3.16)
project(good_stufs LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# ============================================================
# Dependencies (automatically downloaded)
# ============================================================
include(FetchContent)

# --- GLFW ---
FetchContent_Declare(
        glfw
        GIT_REPOSITORY https://github.com/glfw/glfw.git
        GIT_TAG        3.4
        GIT_SHALLOW    TRUE
)
set(GLFW_BUILD_DOCS     OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS    OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
set(GLFW_INSTALL        OFF CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(glfw)

# --- GLAD 2 ---
FetchContent_Declare(
        glad
        GIT_REPOSITORY https://github.com/Dav1dde/glad.git
        GIT_TAG        v2.0.8
        GIT_SHALLOW    TRUE
        SOURCE_SUBDIR  cmake
)
FetchContent_MakeAvailable(glad)

# Generate the loader (change version if you want)
# Available: gl:core=3.3, gl:core=4.1, gl:core=4.5, gl:core=4.6, etc.
glad_add_library(glad_gl_core_46 STATIC REPRODUCIBLE LOADER API gl:core=4.6)

# ============================================================
# Your application
# ============================================================
add_executable(${PROJECT_NAME}
        src/main.cpp          # ← put your source files here
)

target_link_libraries(${PROJECT_NAME} PRIVATE
        glfw
        glad_gl_core_46
)

# On Linux you usually need these system libraries
if(UNIX AND NOT APPLE)
    target_link_libraries(${PROJECT_NAME} PRIVATE dl pthread)
endif()