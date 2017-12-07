#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      data = file.read()
      sum = 0
      for i in range(1, len(data)):
         if (i == len(data) - 1 and data[i] == data[0]):
            sum += int(data[i])
         elif (data[i] == data[i + 1]):
            sum += int(data[i])
      print(sum)


if __name__ == "__main__":
    main()