input = open("input.txt")
lines = input.readlines()

previous = int(lines[0])
increases = 0
for line in lines:
    number = int(line)
    if (number > previous):
        increases += 1
    previous = number
print(increases)




