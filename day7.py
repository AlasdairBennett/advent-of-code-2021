if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))
    lines = [_.replace(" ", "") for _ in lines]

    positions = list(map(int, lines[0].split(",")))

    # part 1
    fuel_costs = []

    for i, pos in enumerate(positions):
        fuel_costs.append(0)
        for pos2 in positions:
            fuel_costs[i] += (abs(pos - pos2))

    print(min(fuel_costs))

    # part 2
    p2_fuel_costs = []

    for i in range(max(positions)):
        p2_fuel_costs.append(0)
        for pos in positions:
            p2_fuel_costs[i] += sum(range(abs(pos - i) + 1))

    print(min(p2_fuel_costs))
