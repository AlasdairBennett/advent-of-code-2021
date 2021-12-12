class Line:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        r = "x1 " + str(self.x1) + " y1 " + str(self.y1) + ", x2 " + str(self.x2) + " y2 " + str(self.y2)
        return r


class LineMap:
    diagram = [[]]

    def __init__(self):
        diagram = [[0]]

    def __repr__(self):
        r = ""
        for ln in self.diagram:
            for elem in ln:
                if elem == 0:
                    r += "."
                else:
                    r += str(elem)
            r += "\n"
        return r

    def add_line(self, ln):
        # Expand diagram to fit new line
        if max(ln.x1, ln.x2) >= len(self.diagram[0]):
            for i in range(max(ln.x1, ln.x2) - len(self.diagram[0]) + 1):
                for row in self.diagram:
                    row.append(0)
        if max(ln.y1, ln.y2) >= len(self.diagram):
            for i in range(max(ln.y1, ln.y2) - len(self.diagram) + 1):
                self.diagram.append([0 for _ in self.diagram[0]])

        # Horizontal line
        if (ln.y1 == ln.y2) and (ln.x1 != ln.x2):
            for i in range(max(ln.x1, ln.x2) - min(ln.x1, ln.x2) + 1):
                self.diagram[ln.y1][min(ln.x1, ln.x2) + i] += 1

        # Vertical line
        if (ln.x1 == ln.x2) and (ln.y1 != ln.y2):
            for i in range(max(ln.y1, ln.y2) - min(ln.y1, ln.y2) + 1):
                self.diagram[min(ln.y1, ln.y2) + i][ln.x1] += 1

        # Diagonal line
        if abs(ln.x1 - ln.x2) == abs(ln.y1 - ln.y2):
            for i in range(abs(ln.x1 - ln.x2) + 1):
                if ln.y1 > ln.y2:
                    if ln.x1 > ln.x2:
                        self.diagram[ln.y2 + i][ln.x2 + i] += 1
                    if ln.x1 < ln.x2:
                        self.diagram[ln.y1 - i][ln.x1 + i] += 1
                if ln.y1 < ln.y2:
                    if ln.x1 > ln.x2:
                        self.diagram[ln.y2 - i][ln.x2 + i] += 1
                    if ln.x1 < ln.x2:
                        self.diagram[ln.y1 + i][ln.x1 + i] += 1

    def count_overlap_points(self):
        overlap_points = 0

        for row in self.diagram:
            for elem in row:
                if elem >= 2:
                    overlap_points += 1

        return overlap_points


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))
    lines = [_.replace(" ", "") for _ in lines]

    lineobjects = []

    for line in lines:
        arrowsplit = list(line.split("->"))
        split1 = list(map(int, arrowsplit[0].split(",")))
        split2 = list(map(int, arrowsplit[1].split(",")))
        lineobjects.append(Line(split1[0], split1[1], split2[0], split2[1]))

    mapobj = LineMap()

    for line in lineobjects:
        mapobj.add_line(line)

    print(mapobj.count_overlap_points())
