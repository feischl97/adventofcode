input = open("input.txt")
lines = input.readlines()

bitcount = [0] * (len(lines[0])-1) # do not inclued /n at end of lines
for line in lines:
    for index in range(0,len(line)):
        bit = line[index]
        if (bit == "1"):
            bitcount[index] += 1

gamma_rate = []
for b in bitcount:
    b = int(b)
    if (b >= len(lines)/2):
        gamma_rate.append("1")
    else:
        gamma_rate.append("0")
    index += 1

epsilon_rate = []
for bit in gamma_rate:
    if (bit == "1"):
        epsilon_rate.append("0")
    else:
        epsilon_rate.append("1")

gamma = int("".join(gamma_rate), 2)
epsilon = int("".join(epsilon_rate), 2)
print(gamma * epsilon)


