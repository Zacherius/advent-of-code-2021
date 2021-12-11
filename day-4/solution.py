# ----------------------------------- PART 1 ----------------------------------
def winner(rows: list) -> bool:
    """
    Check the board to see if it is a winner
    """
    # By default, the board is already a list or rows. We also want to check
    # columns, so get a list of columns as well
    columns = [list(column) for column in list(zip(*rows))]

    # combine the rows and columns into one super list, and see if there is a
    # winning combo in it
    return (["X"] * 5) in (rows + columns)


def play_bingo(numbers, boards) -> tuple:
    """
    Play bingo against all the provided boards, get the board that would win 
    first, and the board that would win last
    """
    first_winner = last_winner = 0
    winners = set()
    for number in numbers:
        for index, board in enumerate(boards):
            if index in winners:
                continue
            for row in board:
                if number in row:
                    row[row.index(number)] = "X"
            if winner(board):
                if not first_winner:
                    first_winner = calculate_score(board, number)
                last_winner = calculate_score(board, number)
                # basically remove the board from play
                winners.add(index)

    return first_winner, last_winner


def calculate_score(board, num) -> int:
    return num * sum([item for sublist in board for item in sublist if item != "X"])


# read the data for day-4
with open("day-4/data.txt", "r") as data_file:
    data = [line.strip() for line in data_file.readlines()]

# extract the numbers to draw
numbers_to_draw = map(int, data[0].split(','))

# and the bingo boards from the data
bingo_boards = list()
for i in range(2, len(data), 6):
    bingo_boards.append([list(map(int, line.split())) for line in data[i:i+5]])

result = play_bingo(numbers_to_draw, bingo_boards)
print(f"Part1: {result[0]} \nPart2: {result[1]}")
