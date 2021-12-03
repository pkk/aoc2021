def day3_a(arr):
    g, e = "", ""
    for i in range(len(arr[0])):
        col = [row[i] for row in arr]
        g += max(set(col), key=col.count)
        e += min(set(col), key=col.count)
    print(int(g, 2) * int(e, 2))


def day3_b(inp_arr, is_oxygen):
    for i in range(len(inp_arr[0])):
        col = [row[i] for row in inp_arr]
        g, e = "", ""
        g += max(set(col), key=col.count)
        e += min(set(col), key=col.count)
        m = g if is_oxygen else e
        if g != e:
            inp_arr = [x for x in inp_arr if x[i] == m]
        else:
            inp_arr = [x for x in inp_arr if x[i] == ("1" if is_oxygen else "0")]
        if len(inp_arr) == 1:
            return "".join(inp_arr)


if __name__ == "__main__":
    data = open("day3.txt").read().strip().split("\n")
    day3_a(data)
    oxygen = day3_b(data, True)
    co2 = day3_b(data, False)
    print(int(oxygen, 2) * int(co2, 2))
