## Day 1: Trebuchet? 


def convert_words_to_num(line: str):
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

    for i in  words_array.keys():
        line = line.replace(i, words_array[i])

    return line        

def find_first_number(line: str): 
    for i in line:
        if i >= '0'  and i <= '9':
            return int(i)


with open("sample2") as input_file:
    lines = input_file.readlines()

print(lines)

sum = 0
new_count = 0
for l in lines:
    # first_number, last_number = [find_first_number(l), find_first_number(reversed(l))]
    # count = first_number * 10 + last_number
    # sum += count
    # count = 0
    new_line = convert_words_to_num(l)
    print(new_line)
    first_number, last_number = [find_first_number(new_line), find_first_number(reversed(new_line))]
    print(first_number, last_number)
    count = first_number * 10 + last_number
    new_count += count

print(sum)
