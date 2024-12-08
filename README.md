# Rover
This is a solution for Rover problem by python and its unit test by pytest package

## Problem Statement
You are building a rover that is going to explore Mars (represented as a grid).

The initial starting point of a rover is 0:0:N
0,0 are X and Y coordinates on a grid
‘N’ is the direction rover is facing - alias for North (directions it can face are N, S, E, W)
Rover accepts different commands and returns its position after executing them
‘L’ and ‘R’ commands rotate the rover left and right, respectively
‘M‘ command moves the rover one step in the direction it’s currently facing
To make things simple, assume following:

Rover’s starting point is always 0:0:N
The grid has infinite size, so don’t worry about falling off the grid
Commands the rover will get will always be valid, so no need to guard against invalid input

### Example

The rover receives a string of multiple commands and returns its position after executing commands. 
For example, assuming rover’s starting position is “0:0:N”, sending "RMMLML" to the rover will move it to "2:1:W".

Input "RMMLML"
Output "2:1:W"
0.0N
R 0.0E
M 1.0E
M 2.0E
L 2.0N
M 2.1N
L 2.1W
