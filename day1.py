
# read the input data for day-1
with open("day1-input.txt", "r") as day1_input:
    # convert the input into integers
    readings = [int(num.strip()) for num in day1_input.readlines()]

num_of_increases = 0
previous_reading = readings[0]  # store the first recording as the previous

# starting from the 2nd reading...
for reading in readings[1:]:
    # check to see if the current reading is greater than the previous
    if previous_reading < reading:
        num_of_increases += 1

    # set previous reading to the current reading
    previous_reading = reading

print(num_of_increases)