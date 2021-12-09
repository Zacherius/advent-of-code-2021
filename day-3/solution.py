# ----------------------------------- PART 1 ----------------------------------
# read the data for day-3
with open("day-3/data.txt", "r") as data_file:
    binaries = [binary.strip() for binary in data_file.readlines()]

# make a dictionary to keep track of the number of occurences for each bit
#  from left to right
all_counts = {i: {"0": 0, "1": 0} for i in range(len(binaries[0]))}

# count the 0's and 1's in each binary
for binary in binaries:
    for index, bit in enumerate(binary):
        if bit == "1":
            all_counts[index]["1"] += 1
        else:
            all_counts[index]["0"] += 1

gamma_rate = 0
epsilon_rate = 0
# reverse the counter (this will allow us to read the binary number as if we were
# reading it from right to left), then for each bit, if there were more 0's in the
# posistion, add the bit value to the epsilon, else add the bit value to the gamma
for exponent, counts in enumerate(list(all_counts.values())[::-1]):
    if counts['0'] > counts['1']:
        epsilon_rate += (2 ** exponent)

    else:
        gamma_rate += (2 ** exponent)

print(f"Power Consumption: {gamma_rate * epsilon_rate}")

# ----------------------------------- PART 2 ----------------------------------
# store all the binaries in two lists, one for oxygen generator rating and one
# for c02 scrubber rating
oxygen_binaries = binaries
c02_binaries = binaries
bit = 0
while True:
    # to get the oxygen generator rating, determine the most common value
    # (0 or 1) in the current bit position, and keep only numbers with that bit
    # in that position. If 0 and 1 are equally common, keep values with a 1 in
    # the position being considered
    oxygen_0 = 0
    oxygen_1 = 0

    # get the most common value in the current bit posistion while there are
    # more than 1 binaries
    if len(oxygen_binaries) > 1:
        for binary in oxygen_binaries:
            if binary[bit] == "0":
                oxygen_0 += 1
            else:
                oxygen_1 += 1
        oxygen_bit = "1" if oxygen_0 <= oxygen_1 else "0"

        oxygen_binaries = [
            binary for binary in oxygen_binaries if binary[bit] == oxygen_bit
        ]

    # To find CO2 scrubber rating, determine the least common value (0 or 1) in
    # the current bit position, and keep only numbers with that bit in that
    # position. If 0 and 1 are equally common, keep values with a 0 in the position
    # being considered.
    c02_0 = 0
    c02_1 = 0

    # get the least common value in the current bit posistion while there are
    # more than 1 binaries
    if len(c02_binaries) > 1:
        for binary in c02_binaries:
            if binary[bit] == "0":
                c02_0 += 1
            else:
                c02_1 += 1
        c02_bit = "0" if c02_0 <= c02_1 else "1"

        c02_binaries = [
            binary for binary in c02_binaries if binary[bit] == c02_bit
        ]

    # if the binaries for each rating have been determined, stop the search
    if len(oxygen_binaries) <= 1 and len(c02_binaries) <= 1:
        break

    else:  # increase the bit position
        bit += 1

# convert the binary to a decimal value
life_support_rating = int(oxygen_binaries[0], 2) * int(c02_binaries[0], 2)
print(f"life support rating: {life_support_rating}")
