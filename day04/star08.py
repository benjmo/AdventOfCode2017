#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      numValid = 0
      for line in file:
         currWords = []
         valid = True
         for word in line.replace('\n', '').split(' '):
            if (''.join(sorted(word)) in currWords):
               valid = False
               break;
            currWords.append(''.join(sorted(word)))

         if (valid):
            numValid += 1

      print(numValid)


if __name__ == "__main__":
    main()