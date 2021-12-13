"""
Credit goes to /u/joshbduncan for the super elegant modulo solution
"""

if __name__ == "__main__":
    # read the data for day-6
    with open("day-6/data.txt", "r") as data_file:
        timer_values = list(map(int, data_file.read().split(",")))

    # timer_values = list(map(int, "3,4,3,1,2".split(",")))

    # brute force method (quick and easy to develop, terrible for memory
    # (I had 1,765,974,267,455 fishes in timer_values when it was all
    #  said and done)
    # for _ in range(80):
    #     data_length = len(timer_values)
    #     for i in range(data_length):
    #         # if the internal timer is 0, set it to 6 and append an 8
    #         if timer_values[i] == 0:
    #             timer_values[i] = 6
    #             timer_values.append(8)

    #         else:  # otherwise count the timer down
    #             timer_values[i] -= 1

    # print(len(timer_values))

    # get the initial occurences for each internal timer value
    # ex: if init_timer_values = [3,4,3,1,2]
    #     then timer_occurences = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    timer_occurences = [timer_values.count(i) for i in range(9)]

    for day in range(256):
        if day == 80:  # print solution for part 1
            print(f"Part 1: {sum(timer_occurences)}")

        # add any additional fish (if any) into the population
        # NOTE: if you keep track of the actual fish and their timers
        #  (see Visual Aid) then you will notice that the timer occurences
        #  do not match up with the fish interal timers after the first
        #  day. That's okay though, it's only keeping track of the actual
        #  population, which is accurate.
        timer_occurences[(day + 7) % 9] += timer_occurences[day % 9]

        # Visual Aid:
        # after Day 0: [2,3,2,0,1]
        # timer_occurences[(0 + 7) % 9] += timer_occurences[0 % 9]
        # timer_occurences = [0, 1, 1, 2, 1, 0, 0, 0, 0]
        #
        # after Day 1: [1,2,1,6,0,8]
        # timer_occurences[(1 + 7) % 9] += timer_occurences[1 % 9]
        # timer_occurences = [0, 1, 1, 2, 1, 0, 0, 0, 1]
        #
        # after Day 2: [0,1,0,5,6,7,8]
        # timer_occurences[(2 + 7) % 9] += timer_occurences[2 % 9]
        # timer_occurences = [1, 1, 1, 2, 1, 0, 0, 0, 1]
        #
        # after Day 3: [6,0,6,4,5,6,7,8,8]
        # timer_occurences[(3 + 7) % 9] += timer_occurences[3 % 9]
        # timer_occurences = [1, 1, 1, 2, 1, 0, 0, 0, 1]

    print(f"Part 2: {sum(timer_occurences)}")
