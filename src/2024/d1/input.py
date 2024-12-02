with open('input.txt', 'r') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = map(int, line.strip().split())
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

differences = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(differences))

similarity_score = 0
for num in list1:
    count = list2.count(num)
    similarity_score += num * count

print(similarity_score)

