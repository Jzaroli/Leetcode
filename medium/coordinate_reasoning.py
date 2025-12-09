"""
Problem: Minimum Steps to Reach Target with Diagonal Moves

You are standing at point (0, 0) on an infinite 2D grid.
You want to reach a target point (x, y).

At each move, you may:

Move 1 unit horizontally (left or right),

Move 1 unit vertically (up or down), or

Move 1 unit diagonally, meaning move (+1, +1), (+1, -1), (-1, +1), or (-1, -1).

Return the minimum number of steps needed to reach (x, y).
"""

def find_moves(x, y):
    return max(abs(x), abs(y))
          
print(find_moves(-5, 8))
print(find_moves(-5, -8))
print(find_moves(5, -8))
print(find_moves(5, 8))


