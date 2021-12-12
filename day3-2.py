lines = open("input.txt").readlines()
isOxygen = True

def most_common_at_index(index, list):
    count = 0
    for var in list:
        if (var[index] == "1"):
            count += 1
    if (count >= len(list)/2):
        return "1"
    else:
        return "0"

def least_common_at_index(index, list):
    count = 0
    for var in list:
        if (var[index] == "1"):
            count += 1
    if (count < len(list)/2):
        return "1"
    else:
        return "0"

def filter_fun():
    arr = lines.copy()
    for index in range(12):
        if (len(arr) == 1): return arr[0]
        bit = most_common_at_index(index, arr) if isOxygen else least_common_at_index(index, arr)
        for line in lines:
            if (line[index] != bit):
                try:
                    arr.remove(line)
                except ValueError:
                    pass
    return arr[0]

def main():
    oxygen = filter_fun()
    global isOxygen
    isOxygen = False
    co2 = filter_fun()
    print(int(oxygen, 2) * int(co2, 2))
    
if __name__ == "__main__":
    main()