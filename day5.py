def parse_file():
    co_ordinates = []
    with open("day5.txt") as f:
        raw_lines = f.readlines()
    for a_line in raw_lines:
        a, b = a_line.split("->")
        x1, y1 = list(map(int, a.split(",")))
        x2, y2 = list(map(int, b.split(",")))
        co_ordinates.append((x1, y1, x2, y2))
    return co_ordinates


def day5_1(inp):
    point_map = dict()

    for (x1, y1, x2, y2) in inp:

        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:

            for y in range(min(y1, y2), max(y1, y2) + 1):
                point_map[(x1, y)] = point_map.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point_map[x, y1] = point_map.get((x, y1), 0) + 1

    ans = 0
    for point in point_map:
        intersections = point_map[point]
        ans += 1 if intersections >= 2 else 0

    print(f"Day 5 part 1 ans {ans}")


def day5_2(inp):
    point_map = dict()

    for (x1, y1, x2, y2) in inp:
        x_inc = 0
        y_inc = 0
        if x1 < x2:
            x_inc = 1
        elif x1 > x2:
            x_inc = -1
        if y1 < y2:
            y_inc = 1
        elif y1 > y2:
            y_inc = -1

        while (x1, y1) != (x2, y2):
            point_map[(x1, y1)] = point_map.get((x1, y1), 0) + 1
            x1 += x_inc
            y1 += y_inc
        point_map[(x2, y2)] = point_map.get((x2, y2), 0) + 1
    ans = 0
    for point in point_map:
        intersections = point_map[point]
        ans += 1 if intersections >= 2 else 0

    print(f"Day 5 part 2 ans {ans}")


if __name__ == "__main__":
    coords = parse_file()
    day5_1(coords)
    day5_2(coords)
