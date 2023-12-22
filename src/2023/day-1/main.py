## Day 1: Trebuchet?
import argparse

words_array = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def convert_words_to_num_gen(line: str, part_two: bool = False):
    first_digit = -1
    last_digit = -1
    for i in range(0, len(line)):
        if line[i].isdigit():
            if first_digit == -1:
                first_digit = int(line[i])
                continue
            last_digit = int(line[i])
            continue
        if part_two == True:
            for j in range(0, len(line)+1):
                if line[i:j] in words_array.keys():
                    if first_digit == -1:
                        first_digit = int(words_array[line[i:j]])
                        i += j
                        break
                    else:
                        last_digit = int(words_array[line[i:j]])
    if last_digit == -1:
        last_digit = first_digit

    return first_digit, last_digit

def main():
    parser = argparse.ArgumentParser(description='')

    # Adding positional arguments
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--enable_part_two', help="enable or disable for part two", required=False)

    # Parsing the arguments
    args = parser.parse_args()

    # Accessing the values
    input_file = args.input_file
    enable_part_two = True if args.enable_part_two == 'True' else False

    with open(input_file) as file:
        lines = file.readlines()

    sum = 0
    for l in lines:
        f,l = convert_words_to_num_gen(l, enable_part_two)
        sum += ((f * 10) + l)
    print(sum)


if __name__ == '__main__':
    main()
