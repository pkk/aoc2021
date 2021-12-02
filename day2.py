def read_file():
    with open('day2.txt') as f:
        lines = f.readlines()
    return lines

def day2_a(lines):
    depth, height = 0, 0 
    for line in lines:
        arr = line.split()
        if arr[0] == "up":
            depth -= int(arr[1])
        elif arr[0] == "down":
            depth += int(arr[1])
        else:
            height += int(arr[1])
    return depth * height

def day2_b(lines):
    d,h,a = 0,0,0
    for line in lines:
        arr = line.split()
        if arr[0] == "up":
            a -= int(arr[1])
        elif arr[0] == "down":
            a += int(arr[1])
        else:
            h += int(arr[1])
            d += a * int(arr[1])
    return d * h
            
if __name__ == "__main__":
    lines = read_file()
    print("Day 2 a:", day2_a(lines))
    print("Day 2 b:", day2_b(lines))