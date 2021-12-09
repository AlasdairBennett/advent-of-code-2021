def scan_file(filename):
    fo = open(filename)
    return fo.readlines()


# returns the most common bit at a given position
def most_common_bit(bitlines, pos):
    zerocount = 0
    onecount = 0
    for line in bitlines:
        if line[pos] == '0':
            zerocount += 1
        if line[pos] == '1':
            onecount += 1

    if zerocount > onecount:
        return 0
    elif zerocount < onecount:
        return 1
    else:
        return 1


def oxygen_generator_rating(bitlines):
    bitlines_copy = bitlines[:]
    bitlines_next = []
    for i, b in enumerate(bitlines[0]):
        if len(bitlines_copy) == 1:
            return bitlines_copy[0]
        mcb = most_common_bit(bitlines_copy, i)
        for line in bitlines_copy:
            if line[i] != str(mcb):
                bitlines_next.append(line)
        for line in bitlines_next:
            bitlines_copy.remove(line)
        bitlines_next = []

    if len(bitlines_copy) > 1:
        print("error?")
    return bitlines_copy[0]


def co2_scrubber_rating(bitlines):
    bitlines_copy = bitlines[:]
    bitlines_next = []
    for i, b in enumerate(bitlines[0]):
        if len(bitlines_copy) == 1:
            return bitlines_copy[0]
        mcb = most_common_bit(bitlines_copy, i)
        for line in bitlines_copy:
            if line[i] == str(mcb):
                bitlines_next.append(line)
        for line in bitlines_next:
            bitlines_copy.remove(line)
        bitlines_next = []

    if len(bitlines_copy) > 1:
        print("error?")
    return bitlines_copy[0]


if __name__ == '__main__':
    lines = scan_file("input.txt")
    lines = list(map(str.strip, lines))

    power_consumption = 0
    gamma_rate = ""
    epsilon_rate = ""

    for bitpos, bit in enumerate(lines[0]):
        if bit == "\n":
            continue
        if most_common_bit(lines, bitpos) == 0:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
        else:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    power_consumption = epsilon_rate * gamma_rate
    print("power consumption: " + str(power_consumption))

    co2_rating = int(co2_scrubber_rating(lines), 2)
    oxygen_rating = int(oxygen_generator_rating(lines), 2)
    life_support_rating = co2_rating * oxygen_rating
    print("life support rating: " + str(life_support_rating))
