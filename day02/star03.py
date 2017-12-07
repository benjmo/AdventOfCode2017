#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      sum = 0
      for line in file:
         numbers = line.split();
         numbers = list(map(int, numbers))
         sum += abs(max(numbers) - min(numbers))
      print(sum)

if __name__ == "__main__":
    main()