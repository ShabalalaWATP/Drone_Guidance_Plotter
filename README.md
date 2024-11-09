# Drone_Guidance_Plotter

## Drone Guidance Plotter
A Python program that plots and validates drone routes based on coordinate instructions from input files.

## Description
This program reads route instruction files and plots drone paths on a 12x12 grid. It validates routes to ensure they stay within the grid boundaries and provides visual representation of the path along with coordinates.

## Features

Plots routes on a 12x12 grid
Validates route boundaries
Displays route coordinates
Visual grid representation with:

'S' marking start position
'+' showing the route path
'E' marking end position
'.' for empty grid spaces



## Usage

Place route instruction files in the same directory as the program
Run the program:
Copypython drone_guidance.py

Enter route file name when prompted (e.g., "Route001.txt")
Enter "STOP" to exit the program

## Route File Format
Route files should contain:

Line 1: X-Coordinate of start position
Line 2: Y-Coordinate of start position
Following lines: Direction instructions (N, S, E, or W)

Example route file:
Copy3
12
S
S
W
E
N

## Sample Files
Three test route files are included:

Route001.txt - Valid route example
Route002.txt - Another valid route example
Route003.txt - Invalid route example (goes outside grid)

## Requirements

Python 3.x
No additional libraries required

## Error Handling
The program handles several error cases:

Invalid file names
Routes that would go outside the grid
Invalid direction instructions
