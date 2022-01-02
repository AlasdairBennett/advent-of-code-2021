class OctopusCave:
    octopuses = [[0]]
    flash_total = 0

    def __init__(self, octopus_list):
        self.octopuses = []
        self.flash_total = 0
        for octo_index, octo_row in enumerate(octopus_list):
            self.octopuses.append([])
            for octo_val in octo_row:
                self.octopuses[octo_index].append(int(octo_val))

    def __repr__(self):
        retstr = ""
        for row in self.octopuses:
            retstr += str(row)
            retstr += "\n"
        return retstr

    def step(self):
        # add 1 to all octopus energy levels
        for row_index, row in enumerate(self.octopuses):
            for col_index, octopus in enumerate(row):
                self.octopuses[row_index][col_index] += 1

        for row_index, row in enumerate(self.octopuses):
            for col_index, octopus in enumerate(row):
                if octopus == 10:
                    self.flash(row_index, col_index)

        # set flashed octopi to 0
        is_all_flash = True
        for row_index, row in enumerate(self.octopuses):
            for col_index, octopus in enumerate(row):
                if octopus > 9:
                    self.octopuses[row_index][col_index] = 0
                else:
                    is_all_flash = False
        if is_all_flash:
            return True
        return False

    def flash_check(self, row_ind, col_ind):
        if row_ind < 0 or col_ind < 0:
            return
        if row_ind > len(self.octopuses)-1:
            return
        if col_ind > len(self.octopuses[row_ind])-1:
            return

        if self.octopuses[row_ind][col_ind] == 10:
            self.flash(row_ind, col_ind)
        self.octopuses[row_ind][col_ind] += 1
        if self.octopuses[row_ind][col_ind] == 10:
            self.flash(row_ind, col_ind)

    def flash(self, row_ind, col_ind):
        self.flash_total += 1
        self.octopuses[row_ind][col_ind] += 1
        self.flash_check(row_ind-1, col_ind-1)
        self.flash_check(row_ind-1, col_ind)
        self.flash_check(row_ind-1, col_ind+1)
        self.flash_check(row_ind, col_ind-1)
        self.flash_check(row_ind, col_ind+1)
        self.flash_check(row_ind+1, col_ind-1)
        self.flash_check(row_ind+1, col_ind)
        self.flash_check(row_ind+1, col_ind+1)


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    cave = OctopusCave(lines)
    for i in range(100):
        cave.step()
    print(cave.flash_total)

    cave = OctopusCave(lines)
    step_num = 0
    while not cave.step():
        step_num += 1
    print(step_num + 1)
