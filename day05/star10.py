#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      instructions = list(map(int, file.read().split('\n')))
      pos = 0
      i = 0
      while (pos >= 0 and pos < len(instructions)):
         oldPos = pos
         pos += instructions[pos]
         if (instructions[oldPos] < 3):
            instructions[oldPos] += 1
         else:
            instructions[oldPos] -= 1
         i += 1
      print(i)


if __name__ == "__main__":
    main()