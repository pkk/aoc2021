def sol(a_list):
    return sum( 1 if a_list[x] > a_list[x-1] else 0 for x in range(1,len(a_list)))

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