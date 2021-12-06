def day6_1(inps, days):
    fish_spawn_count = {k: 0 for k in range(0, 9)}
    # print(fish_spawn_count)
    for inp in inps:
        fish_spawn_count[inp] += 1
    for i in range(days):
        current_fish_count = fish_spawn_count[0]
        fish_spawn_count[7] += current_fish_count
        # print(fish_spawn_count[7], fish_spawn_count[8])
        for k in range(1, 9):
            # print(fish_spawn_count[k-1])
            fish_spawn_count[k - 1] = fish_spawn_count[k]
        fish_spawn_count[8] = current_fish_count
    print(f"Day6 ans is {sum(fish_spawn_count.values())}")


if __name__ == "__main__":
    with open("day6.txt") as f:
        line = f.readline()
    spawn_seed = [int(x) for x in line.split(",")]
    # print(len(spawn_seed))
    # print(spawn_seed[0:5])
    day6_1(spawn_seed, 80)
    day6_1(spawn_seed, 256)
