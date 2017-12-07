#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      sum = 0
      for line in file:
         numbers = line.split();
         numbers = list(map(int, numbers))
         found = False
         for n in numbers:
            for m in numbers:
               if (n != m and (max(n,m) % min(n, m)) == 0):
                  sum += int(max(n, m) / min(n, m))
                  found = True
                  break
            if (found):
               break
      print(sum)

if __name__ == "__main__":
    main()