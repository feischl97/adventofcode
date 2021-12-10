input = open("input.txt")
lines = input.readlines()

horizontal_pos = 0
vertical_pos = 0
aim = 0

for line in lines:
    movment = line.split(" ")
    direction = movment[0]
    distance = int(movment[1])
    if (direction == "forward"):
        horizontal_pos += distance
        vertical_pos += aim * distance
    elif (direction == "up"):
        aim -= distance
    else:
        aim += distance
print(horizontal_pos*vertical_pos)
        
