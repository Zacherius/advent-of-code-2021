# ----------------------------------- PART 1 ----------------------------------
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


# ----------------------------------- PART 2 ----------------------------------
num_of_increases = 0
previous_sum = sum(readings[0:3])  # store the first sum (first three readings)
# again, starting from the second reading
for i in range(1, len(readings) - 1):
    # if we are unable to get a sum of three readings, exit loop
    if (i + 3) > len(readings):
        break
    
    # get the current sum and compare to the previous
    current_sum = sum(readings[i:i+3])
    if previous_sum < current_sum:
        num_of_increases += 1
    
    # set previous sum to the current sum
    previous_sum = current_sum

print(num_of_increases)