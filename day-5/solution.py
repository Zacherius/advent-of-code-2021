def clean_data(data) -> list:
    """
    Clean the data up by removing "->" and returning a list that contains
    lists that contain the starting coordinates, and the ending coordinates

    :param data: a list that represents the data for this problem
    :return: -> [[(x1, y1), (x2, y2)], ..., [(x1, y1), (x2, y2)]]
    """
    cleaned_data = list()
    for datum in data:
        cleaned_data.append([
            tuple(map(int, datum[0].split(","))),
            tuple(map(int, datum[1].split(",")))
        ])
    return cleaned_data


def min_max(num1, num2) -> tuple:
    """
    Gets the min and max of the provided values

    :param num1: first number
    :param num2: second number
    :return: -> (min, max)
    """
    return (min(num1, num2), max(num1, num2))


if __name__ == "__main__":
    # read the data for day-5
    with open("day-5/data.txt", "r") as data_file:
        data = [line.strip().split(" -> ") for line in data_file.readlines()]

    # used to for testing
    # data_file = """0,9 -> 5,9
    # 8,0 -> 0,8
    # 9,4 -> 3,4
    # 2,2 -> 2,1
    # 7,0 -> 7,4
    # 6,4 -> 2,0
    # 0,9 -> 2,9
    # 3,4 -> 1,4
    # 0,0 -> 8,8
    # 5,5 -> 8,2"""
    # data = [line.strip().split(" -> ") for line in data_file.split("\n")]

    # multiple overlap counter and diagram for part
    overlaps = 0
    diagram = [[0 for j in range(1024)] for i in range(1024)]

    # iterate over each set of coordinates
    for coords in clean_data(data):
        x1, y1 = coords[0]
        x2, y2 = coords[1]

        # get the min and max values (x and y)
        y_min, y_max = min_max(y1, y2)
        x_min, x_max = min_max(x1, x2)

        # horizontal
        if x1 == x2:
            for y in range(y_min, y_max + 1):
                diagram[y][x1] += 1
                if diagram[y][x1] == 2:
                    overlaps += 1

        # vertical
        elif y1 == y2:
            for x in range(x_min, x_max + 1):
                diagram[y1][x] += 1

                if diagram[y1][x] == 2:
                    overlaps += 1

        # Part 2 only (Comment out to get the results for part 1)
        # diagonal
        else:
            # determine the starting y posistion as well as the direction for
            # each step
            if x_min == x1:
                y = y1
                y_step = 1 if y1 < y2 else -1
            else:
                y = y2
                y_step = 1 if y2 < y1 else -1

            y_offset = 0
            for x in range(x_min, x_max + 1):
                diagram[y+y_offset][x] += 1
                if diagram[y+y_offset][x] == 2:
                    overlaps += 1
                y_offset += y_step

    print(overlaps)
