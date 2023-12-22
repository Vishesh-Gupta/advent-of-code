#!/usr/bin/env python3

import argparse

def solution(input_file, gold_star):
    if input_file:
      with open(input_file) as file:
          input = file.readlines()

    # Start coding your solution here
    print("Advent of Code XXXX: Day #X")

def argparser():
    parser = argparse.ArgumentParser(description='Day # :')

    # Adding positional arguments
    parser.add_argument('-file', '--input_file', required=False, help='Path to the input file')
    parser.add_argument('-gold', '--gold_star', help="enable or disable for part two", required=False)

    # Parsing the arguments
    args = parser.parse_args()

    # Accessing the values
    input_file = args.file if args.input_file else ""
    gold_star = True if args.gold_star == 'True' else False
    return args.input_file, gold_star

def main():
    input_file, gold_star = argparser()
    solution(input_file, gold_star)

if __name__ == '__main__':
    main()
