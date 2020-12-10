# Day 4: Scratchcards ---
#

with open("input") as sample:
    input = sample.readlines()


def find_wins(line: str):
    win_nums, my_nums = line.split(":")[1].split("|")
    win_nums = win_nums.strip().split(" ")
    my_nums = my_nums.strip().split(" ")
    count = 0
    print(win_nums, my_nums)
    for num in win_nums:
        if num in my_nums:
            count += 1
    return count

sum = 0
for line in input:
    count = find_wins(line)
    print(count)
    if count >= 1:
        sum += 2 ** (count-1)

print(sum)
