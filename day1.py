def sol(a_list):
    ans = 0
    prev = a_list[0]
    for line in a_list:
        ans = ans + (1 if line > prev else 0)
        prev = line
    return ans

def day1_a(lines):
    return sol(lines)

def day1_b(lines):
    tup_list = []
    x = 0
    while x + 2 < len(lines):
        tup_list.append((lines[x], lines[x+1], lines[x+2]))
        x = x + 1
    tup_list_sum = [x + y + z for (x,y,z) in tup_list]
    return sol(tup_list_sum)

def read_file():
    with open("day1.txt") as f:
        lines = f.readlines()
    return list(map(int, lines))
    

if __name__ == '__main__':
    lines = read_file()
    day1_a_ans = day1_a(lines)
    day1_b_ans = day1_b(lines)
    print("Day 1 - a:", day1_a_ans)
    print("Day 1 - b:", day1_b_ans)