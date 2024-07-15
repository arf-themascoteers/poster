import numpy as np

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])

start_color = hex_to_rgb('#0000FF')
end_color = hex_to_rgb('#FF0000')

colors = np.linspace(start_color, end_color, 10)

print(colors)
