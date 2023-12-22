# --- Day 3: Gear Ratios ---
#
import argparse
from pprint import pprint

def check_neighbours(engine, r, c):
    num_rows, num_cols = len(engine), len(engine[0])
    is_part_number = False
    symbol = False
    for i in range(-1, 2):
        if r-i < 0 or r+i >= num_rows:
            continue
        for j in range(-1, 2):
            if c-j < 0 or c+j >= num_cols:
                continue
            print(f"i: {r+i}, j: {c+j}")
            print(engine[i][j])
            if engine[i][j] == ".":
                continue
            elif engine[i][j].isdigit():
                is_part_number = True
            else:
                print("Hit this case")
                symbol = True
    return is_part_number, symbol


def solution(input_file, enable):
    with open(input_file) as file:
        input: str = file.readlines()

    engine = []
    for line in input:
        engine.append(line.strip())

    count = 0
    pprint(engine)
    rows, cols = len(engine), len(engine[0])
    print(rows, cols)
    for r in range(0, rows):
        part_number = 0
        is_part_number = False
        symbol = False
        for c in range(0, cols):
            print(f"digit: {engine[r][c]}, part_number: {part_number}, count: {count}, symbol: {symbol}, is_part_number: {is_part_number}")
            if engine[r][c] == ".":
                if symbol:
                    count += part_number
                    symbol = False
                    part_number = 0
                is_part_number = False
                continue
            elif engine[r][c].isdigit():
                # Figure out neighbours
                symbol_store = symbol
                is_part_number, symbol  = check_neighbours(engine, r, c)
                if is_part_number and symbol_store:
                    symbol = True
            else:
                continue
            if is_part_number:
                part_number = part_number * 10 + int(engine[r][c])

        print(count)

def argparser():
    parser = argparse.ArgumentParser(description='')

    # Adding positional arguments
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--enable_part_two', help="enable or disable for part two", required=False)

    # Parsing the arguments
    args = parser.parse_args()

    # Accessing the values
    enable_part_two = True if args.enable_part_two == 'True' else False
    return args.input_file, enable_part_two

def main():
    input_file, enabled_part_two = argparser()
    solution(input_file, enabled_part_two)

if __name__ == '__main__':
    main()