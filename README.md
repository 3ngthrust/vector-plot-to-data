# vector-plot-to-data
A short script to convert paths of lines in plots in .svg files into their original values.

Sometimes it is handy to extract the data of plots in .pdf documents or other vector based images with high accuracy.

This script works with solid lines in plots represented by paths.

## How it works

1. Use a vector image manipulation software (e.g. Illustrator) to isolate and delete everything but the line and the axes of the plot. -> Save the manipulated image.

2. In the software select a tick on the x-axis and note its value (e.g. 1 -> tick_1_value) and its x-position on the image (e.g. 77.077 -> tick_1).
   Select another tick on the x-axis as far away as possible, note its value (e.g. 7 -> tick_2_value) and its x-position on the image (e.g. 152.391 -> tick_2)
   
   Do the same for the y-axis.
   
3. Click on the first point of the path of the line -> Note its x (e.g. 55.511) and y (e.g. 103.078) position (-> start_point).  
   Click on the last point of the path of the line -> Note its x (e.g. 174.577) and y (e.g. 149.128) position (-> end_point).
   
4. Delete every element and every layer except the line of the image.

5. Save it as .svg. If the option is presented extend the number of decimal points to 5 or more for increased accuracy while saving.

6. Open the .svg with a text editor and delete all text. Only numbers separated by commas should be left. (Spaces and linebreaks are fine, too.)
   
7. Place the python script where the .svg is and write your filename as textlink into the script.

8. Adapt the arguments of the function "convert_coordinates" to the values noted earlier.

## Hint
For log-scales just use the exponents as values 10^2 -> 2.
