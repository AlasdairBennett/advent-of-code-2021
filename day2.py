def scan_file(filename):
    fo = open(filename)
    return fo.readlines()
5

if __name__ == '__main__':
    commands = scan_file("input.txt")
    horizontalPosition = 0
    depth = 0
    aim = 0
    for command in commands:
        mag = int(command[len(command)-2::])
        # print(command[:len(command)-3:])
        if command[:len(command)-3:] == "forward":
            horizontalPosition += mag
            depth += aim * mag
        if command[:len(command)-3:] == "down":
            # depth += mag
            aim += mag
        if command[:len(command)-3:] == "up":
            # depth -= mag
            aim -= mag
        # print(command)
        # print("horizontal position " + str(horizontalPosition) + " | depth " + str(depth) + " | aim " + str(aim))
            # command[len(command)-2]

    print(horizontalPosition)
    print(depth)
    print(depth * horizontalPosition)