def day1_a(a_list):
    return sum(a_list[x] > a_list[x-1] for x in range(1,len(a_list)))

def day1_b(a):
    return day1_a([sum(a[x-2:x+1]) for x in range(2,len(a))])

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