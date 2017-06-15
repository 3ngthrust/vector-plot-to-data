#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""

import matplotlib.pyplot as plt

def svg_to_list (txtlink):
    f = open(txtlink)
    str_list = f.read().split()  # Space and Break
    x = [float(s.split(',')[0]) for s in str_list]
    y = [float(s.split(',')[1]) for s in str_list]
    return x, y

def convert_coordinates (coordinates, tick_1, tick_1_value, tick_2, tick_2_value, start_point, end_point):    
    # Calculate Software Offset and Scale
    software_scale = (tick_2 - tick_1) / (tick_2_value - tick_1_value)  # =^ length of 1
    software_offset = tick_1 - (tick_1_value * software_scale)          # =^ position of 0
    
    # Calculate Values of start and end point
    start_point_value = (start_point - software_offset) / software_scale
    end_point_value = (end_point - software_offset) / software_scale

    # Calculate Offset and Scale
    scale = (coordinates[-1] - coordinates[0]) / (end_point_value - start_point_value) # coordinates[0] =^ start_point and coordinates[-1] =^ end_point
    offset = coordinates[0] - (start_point_value * scale)
    
    # Convert
    return [(c - offset) / scale for c in coordinates]
    
textlink = 'FILENAME.svg'

x, y = svg_to_list(textlink)

# Convert x-values
x_conv = convert_coordinates(x, 77.077, 1, 152.391, 7, 55.511, 174.577)  # REPLACE WITH VALUES CORRESPONDING TO FILENAME.svg

# Convert y-values
y_conv = convert_coordinates(y, 77.344, 0, 137.029, -8, 103.078, 149.128) # REPLACE WITH VALUES CORRESPONDING TO FILENAME.svg

plt.plot(x_conv, y_conv, linewidth=2, label= 1)

plt.show
