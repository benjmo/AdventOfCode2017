#!/usr/bin/python3

import re

# puzzle input is 361527
INPUT = 361527

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


def main():
   grid = [[0 for i in range(99)] for j in range(99)]
   x = int(99/2)
   y = x

   direction = RIGHT
   grid[x][y] = 1

   x += 1
   grid[x][y] = 1

   while (grid[x][y] < INPUT):
      if ([grid[x + 1][y], grid[x][y + 1], grid[x - 1][y], grid[x][y - 1]].count(0) >= 3):
         direction = (direction + 1) % 4
      
      if (direction == UP):
         y += 1
      elif (direction == LEFT):
         x -= 1
      elif (direction == DOWN):
         y -= 1
      elif (direction == RIGHT):   
         x +=1

      #calulate sum of all adjacent squares
      grid[x][y] = (grid[x - 1][y + 1] + grid[x][y + 1] + grid[x + 1][y + 1] +
                    grid[x - 1][y]     +                  grid[x + 1][y]     +
                    grid[x - 1][y - 1] + grid[x][y - 1] + grid[x + 1][y - 1] )

   print(grid[x][y])

if __name__ == "__main__":
    main()