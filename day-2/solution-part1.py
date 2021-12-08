# ----------------------------------- PART 1 ----------------------------------
#read the data for day-2
with open("day-2/data.txt", "r") as data_file:
    commands = data_file.readlines()

horizontal_pos = 0
depth = 0

# iterate over each command
for command in commands:
    # separate movement and amount
    movement, amount = command.split()
    
    #forward X increases the horizontal position by X units.
    if movement == "forward":
        horizontal_pos += int(amount)

    # down X increases the depth by X units.
    elif movement == "down":
        depth += int(amount)

    # up X decreases the depth by X units.
    elif movement == "up":
        depth -= int(amount)

print(horizontal_pos * depth)

# ----------------------------------- PART 2 ----------------------------------
aim = 0
horizontal_pos = 0
depth = 0

# iterate over each command
for command in commands:
    # separate movement and amount
    movement, amount = command.split()

    #forward X does two things:
    # It increases your horizontal position by X units.
    # It increases your depth by your aim multiplied by X.
    if movement == "forward":
        horizontal_pos += int(amount)
        depth += (aim * int(amount))

    # down X increases your aim by X units.
    elif movement == "down":
        aim += int(amount)

    # up X decreases your aim by X units.
    elif movement == "up":
        aim -= int(amount)

print(horizontal_pos * depth)

