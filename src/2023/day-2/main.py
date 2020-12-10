# --- Day 2: Cube Conundrum ---
#


def check_validity(count, color, red, green, blue):
    if color == "red" and int(count) > red:
        return False
    elif color == "blue" and int(count) > blue:
        return False
    elif color == "green" and int(count) > green:
        return False
    return True

def each_pick(pick: list, red, green, blue):
    count, color = pick.strip().split(" ")
    return check_validity(count, color, red, green, blue)


def is_line_valid(line, red, green, blue):
    game, choices = line.split(":")
    id = game.split(" ")[1]
    
    choices_opt = choices.split(";")
    result = 0
    
    for i in choices_opt:
        for pick in i.split(","):
            if each_pick(pick, red, green, blue) == False:
                return 0
    return int(id)

with open("input") as sample:
    input = sample.readlines()

count = 0
for line in input:
    count += is_line_valid(line, 12, 13, 14)

print(count)
