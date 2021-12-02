def read_file():
    with open('day2.txt') as f:
        lines = f.readlines()
    return lines

def day2(lines):
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
    return h * a, d * h
            
if __name__ == "__main__":
    lines = read_file()
    print("Day 2 a, b:", day2(lines))