class LanternFishSchool:
    fish_timers = [0] * 9

    def __init__(self, lanternlist):
        for timer in lanternlist:
            self.fish_timers[timer] += 1

    def __repr__(self):
        return str(self.fish_timers)

    def pass_day(self):
        num_new_fish = self.fish_timers[0]
        for index, val in enumerate(self.fish_timers):
            if index == 0:
                continue
            self.fish_timers[index - 1] = val
        self.fish_timers[8] = num_new_fish
        self.fish_timers[6] += num_new_fish

    def count_fish(self):
        fish_count = 0
        for fsh in self.fish_timers:
            fish_count += fsh
        return fish_count


class LanternFish:
    fish_timer = 0

    def __init__(self, timer):
        self.fish_timer = timer

    def __repr__(self):
        return str(self.fish_timer)

    def pass_day(self):
        if self.fish_timer == 0:
            self.fish_timer = 6
            return True
        self.fish_timer -= 1
        return False


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))
    lines = [_.replace(" ", "") for _ in lines]

    # slow version for part 1
    initial_fish = [LanternFish(_) for _ in list(map(int, lines[0].split(",")))]
    for i in range(80):
        new_fish = 0
        for fish in initial_fish:
            if fish.pass_day():
                new_fish += 1
        for j in range(new_fish):
            initial_fish.append(LanternFish(8))

    print(initial_fish)
    print(len(initial_fish))

    # fast version for part 2
    fish_list = LanternFishSchool(list(map(int, lines[0].split(","))))
    for i in range(256):
        fish_list.pass_day()

    print(str(fish_list.count_fish()))
