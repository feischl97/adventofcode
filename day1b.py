def get_number(list, index):
    return int(list[index])

input = open("input.txt")
lines = input.readlines()

previous = get_number(lines, 0) + get_number(lines, 1) + get_number(lines, 2)
increases = 0

list_length = len(lines)
for line in range(0, list_length - 2):
    sum = get_number(lines, line) + get_number(lines, line+1) + get_number(lines, line+2)
    if (sum > previous):
        increases += 1
    previous = sum
print(increases)