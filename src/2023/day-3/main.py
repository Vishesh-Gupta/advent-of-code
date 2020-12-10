# --- Day 3: Gear Ratios ---
#
from pprint import pprint

with open("sample") as sample:
    input = sample.readlines()

pprint(input)

r, c = len(input), len(input[0])
print(r, c)

engine = [['.'*c]*r]

print(input[0][0])

pprint(engine)
