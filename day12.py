class Cave:
    cave_name = ""
    is_large = False
    is_start = False
    is_end = False
    edges = []

    def __init__(self, cave_name):
        self.cave_name = cave_name
        self.edges = []
        if cave_name == 'start':
            self.is_start = True
        elif cave_name == 'end':
            self.is_end = True
        elif cave_name.isupper():
            self.is_large = True

    def __repr__(self):
        retstr = self.cave_name
        retstr += ": "
        for cave in self.edges:
            retstr += cave.cave_name
            retstr += ", "
        return retstr

    def add_edge(self, edge_cave):
        if edge_cave.cave_name not in self.edges:
            self.edges.append(edge_cave)


def depth_first_search(cave, cave_path, finished_paths):
    cave_path.append(cave.cave_name)
    if cave.is_end:
        finished_paths.append(str(cave_path))
        cave_path.pop()
        return finished_paths
    for adjacent_cave in cave.edges:
        if adjacent_cave.is_large or (adjacent_cave.cave_name not in cave_path):
            depth_first_search(adjacent_cave, cave_path, finished_paths)
    cave_path.pop()
    return finished_paths


def depth_first_search_two_small_caves(cave, cave_path, finished_paths, cave_allowed):
    cave_path.append(cave.cave_name)
    if cave.is_end:
        finished_paths.append(str(cave_path))
        cave_path.pop()
        return finished_paths
    for adjacent_cave in cave.edges:
        if adjacent_cave.is_large or (adjacent_cave.cave_name not in cave_path):
            depth_first_search_two_small_caves(adjacent_cave, cave_path, finished_paths, cave_allowed)
        elif (adjacent_cave.cave_name in cave_path) and cave_allowed and adjacent_cave.cave_name != "start":
            depth_first_search_two_small_caves(adjacent_cave, cave_path, finished_paths, False)
    cave_path.pop()
    return finished_paths


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    start_cave = Cave('start')
    cave_list = [start_cave]

    for line in lines:
        edge = line.split('-')
        if not any(cave.cave_name == edge[0] for cave in cave_list):
            cave_list.append(Cave(edge[0]))
        if not any(cave.cave_name == edge[1] for cave in cave_list):
            cave_list.append(Cave(edge[1]))
        for cave in cave_list:
            if cave.cave_name == edge[0]:
                for c in cave_list:
                    if c.cave_name == edge[1]:
                        cave.add_edge(c)
                        c.add_edge(cave)

    paths = depth_first_search(start_cave, [], [])
    print(len(paths))

    paths = depth_first_search_two_small_caves(start_cave, [], [], True)
    print(len(paths))
