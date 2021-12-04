# with open("day4.txt") as f:
#    nums = map(int, f.readline().strip().split(","))
#
#    boards = []
#    board = []
#    for row in f:
#        if board

# with open("day4.txt") as file:
#    bingo_numbers = list(map(int, next(file).split(",")))
#
#    boards = []
#    for row in file:
#        row = row.strip()
#        if row == "":
#            board = []
#            boards.append(board)
#            continue
#        board += map(int, row.split())
#
#    print(boards[0])


def board_wins(a_board):
    for i in range(0, 5):
        if all(n < 0 for n in a_board[5 * i : 5 * i + 5]):
            return True
        if all(n < 0 for n in a_board[i::5]):
            return True
    return False


def day4_1(nums, boards):
    for num in nums:
        for i in range(len(boards)):
            boards[i] = [n if n != num else -1 for n in boards[i]]
            if board_wins(boards[i]):
                return num * sum(n for n in boards[i] if n >= 0)


def day4_2(nums, boards):
    for num in nums:
        won = []
        for i in range(len(boards)):
            boards[i] = [x if x != num else -1 for x in boards[i]]
            has_board_won = board_wins(boards[i])
            if has_board_won and len(boards) == 1:
                return num * sum(x for x in boards[i] if x >= 0)
            if has_board_won:
                won.append(boards[i])
        for board in won:
            boards.remove(board)


if __name__ == "__main__":
    numbers = boards = []
    with open("day4.txt") as f:
        numbers = list(map(int, f.readline().strip().split(",")))
        f.readline()  # empty line
        board = ""
        for line in f:
            if line.strip() != "":
                board += line.strip() + " "
                continue
            else:
                boards.append(list(map(int, board.split())))
                board = ""
    print(day4_1(numbers, boards))
    print(day4_2(numbers, boards))
