# --- Day 2: Cube Conundrum ---
#
import argparse

def check_validity(count, color, red, green, blue):
    if color == "red" and count > red:
        return False
    elif color == "blue" and count > blue:
        return False
    elif color == "green" and count > green:
        return False
    return True

def each_pick(pick: list):
    count, color = pick.strip().split(" ")
    return int(count), color

def is_line_valid(line, red, green, blue):
    game, choices = line.split(":")
    id = game.split(" ")[1]

    choices_opt = choices.split(";")

    for i in choices_opt:
        for pick in i.split(","):
            count, color = each_pick(pick)
            if check_validity(count, color, red, green, blue) == False:
                return 0
    return int(id)

def fewest_count(line: str):
    game, choices = line.split(":")
    id = game.split(" ")[1]

    red = blue = green = 1
    choices_opt = choices.split(";")
    for i in choices_opt:
        for pick in i.split(","):
            count, color = each_pick(pick)
            if color == "blue" and count > blue:
                blue = count
            elif color == "red" and count > red:
                red = count
            elif color == "green" and count > green:
                green = count
    return red, blue, green


def solution(input_file, enabled_part_two):
    with open(input_file) as file:
        input = file.readlines()

    part_one_count = part_two_count = 0

    for line in input:
        part_one_count += is_line_valid(line, 12, 13, 14)
        fewest_red, fewest_blue, fewest_green = fewest_count(line)
        part_two_count += fewest_red * fewest_green * fewest_blue

    print(part_one_count)
    if enabled_part_two:
        print(part_two_count)

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
