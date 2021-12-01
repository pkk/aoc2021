def sol(a_list):
    ans = 0
    prev = a_list[0]
    for line in a_list:
        ans = ans + (1 if line > prev else 0)
        prev = line
    return ans

def day1_a():
    with open("day1.txt") as f:
        lines = f.readlines()
    lines = list(map(int, lines))
    return sol(lines)

def day1_b():
    with open("day1.txt") as f:
        lines = f.readlines()
    lines = list(map(int, lines))
    tup_list = []
    x = 0
    while x + 2 < len(lines):
        tup_list.append((lines[x], lines[x+1], lines[x+2]))
        x = x + 1
    tup_list_sum = [x + y + z for (x,y,z) in tup_list]
    return sol(tup_list_sum)

if __name__ == '__main__':
    day1_a_ans = day1_a()
    print("Day 1 - a:", day1_a_ans)
    day1_b_ans = day1_b()
    print("Day 1 - b:", day1_b_ans)