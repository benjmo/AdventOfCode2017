#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      data = file.read()
   memory = list(map(int, data.split()))
   
   visited = {}
   memString = ' '.join(list(map(str, memory)))
   visited[memString] = 0

   cycles = 0
   while True:
      maxPos = memory.index(max(memory))
      maxMem = memory[maxPos]
      memory[maxPos] = 0

      currPos = (maxPos + 1) % len(memory)
      for i in range(maxMem, 0, -1):
         memory[currPos] += 1
         currPos = (currPos + 1) % len(memory)
      cycles += 1
      
      memString = ' '.join(list(map(str, memory)))
      if (memString in visited):
         print(cycles - visited[memString])
         break
      else:
         visited[memString] = cycles


if __name__ == "__main__":
    main()