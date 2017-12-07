#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      data = file.read()
      sum = 0
      offset = len(data)/2
      for i in range(1, len(data)):
         j = int((i + offset) % len(data))
         if (data[i] == data[j]):
            sum += int(data[i])
      print(sum)


if __name__ == "__main__":
    main()