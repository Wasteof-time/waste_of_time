#version 330 core

out vec4 FragColor;
uniform float u_time;

in vec4 vertex_color;

void main() {
    float green = sin(u_time) * 0.5 + 0.5;
    float red = sin(u_time + 90) * 0.5 + 0.5;
    float blue = cos(u_time) * 0.5 + 0.5;
    FragColor = vec4(red * (vertex_color.x + 0.5), green * (vertex_color.y + 0.5), blue * (vertex_color.x + 0.5), 1.0);
}
