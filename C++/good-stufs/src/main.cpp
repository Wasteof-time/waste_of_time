#include <glad/gl.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <fstream>
#include <sstream>

std::string shader_file_import(const std::string& file_path) {
    std::ifstream file(file_path, std::ios::in | std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Failed to open shader: " << file_path << std::endl;
        return "";
    }
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

int main() {
    //some init stuffs
    if (!glfwInit()) return -1;
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 6);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    GLFWwindow* window = glfwCreateWindow(1280, 720, "OpenGL + GLFW + GLAD", nullptr, nullptr);
    if (!window) {
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    if (!gladLoadGL(glfwGetProcAddress)) {
        std::cerr << "Failed to initialize GLAD\n";
        return -1;
    }
    std::cout << "OpenGL " << glGetString(GL_VERSION) << std::endl;


    // our vertices
    float vertices[] = {
        -0.5f, -0.5f, 0.0f,
         0.5f, -0.5f, 0.0f,
         0.0f,  0.5f, 0.0f
    };

    // vertex shader import
    std::string vertex_shader_string = shader_file_import("../shaders/sh1.vert");
    std::string fragment_shader_string = shader_file_import("../shaders/sh1.frag");

    const char * vertex_shader = vertex_shader_string.c_str();
    const char * fragment_shader = fragment_shader_string.c_str();

    // VBO
    unsigned int VBO;
    glGenBuffers(1, &VBO);

    // VAO
    unsigned int  VAO;
    glGenVertexArrays(1 ,&VAO);
    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER , VBO);
    glBufferData(GL_ARRAY_BUFFER , sizeof(vertices) , vertices , GL_STATIC_DRAW);

    glVertexAttribPointer(0 , 3 , GL_FLOAT , GL_FALSE, 3* sizeof(float) , nullptr);
    glEnableVertexAttribArray(0);
    glBindVertexArray(0);

    // adding shaders into the place
    unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);

    glShaderSource(vertexShader , 1 , &vertex_shader ,NULL);
    glShaderSource(fragmentShader , 1 , &fragment_shader , NULL);
    glCompileShader(vertexShader);
    glCompileShader(fragmentShader);


    // creating shader program
    unsigned int shaderProgram ;
    shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram , vertexShader);
    glAttachShader(shaderProgram , fragmentShader);
    glLinkProgram(shaderProgram);









    while (!glfwWindowShouldClose(window)) {
        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES , 0 , 3);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }


    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);
    glfwTerminate();
    return 0;
}
