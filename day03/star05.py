#!/usr/bin/python3

import re

# puzzle input is 361527
INPUT = 361527

def main():
   i = 1
   while True:
      if (i * i > INPUT):
         i -= 2
         break
      i += 2

   corner = i * i
   length = i
   halfLength = int(i/2) + 1
   
   while (corner + length - 1 < INPUT):
      corner = corner + length - 1

   startPos = corner
   increasing = False
   if (corner + halfLength -1 < INPUT):
      increasing = True
      startPos = corner + halfLength - 1

   dist = halfLength - 1
   while (startPos != INPUT):
      startPos += 1
      if (increasing):
         dist += 1
      else:
         dist -= 1

   print(dist)

if __name__ == "__main__":
    main()