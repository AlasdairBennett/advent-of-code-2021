class TransparentPaper:
    paper = [[]]

    def __init__(self):
        self.paper = [[0]]

    def __repr__(self):
        r = ""
        for ln in self.paper:
            for elem in ln:
                if elem == 0:
                    r += "."
                else:
                    r += "#"
            r += "\n"
        return r

    def add_dot(self, x_coord, y_coord):
        if y_coord >= len(self.paper):
            for i in range(y_coord - len(self.paper) + 1):
                self.paper.append([0 for _ in self.paper[0]])
        if x_coord >= len(self.paper[0]):
            for i in range(x_coord - len(self.paper[0]) + 1):
                for paper_row in self.paper:
                    paper_row.append(0)
        self.paper[y_coord][x_coord] = 1

    def fold_up(self, y_coord):
        for i in range(y_coord):
            for dot_index, dot in enumerate(self.paper[i]):
                self.paper[i][dot_index] += self.paper[-(i+1)][dot_index]
        del self.paper[y_coord:]

    def fold_left(self, x_coord):
        for row in self.paper:
            for i in range(x_coord):
                row[i] += row[-(i+1)]
        for row in self.paper:
            del row[x_coord:]

    def count_dots(self):
        total = 0
        for row in self.paper:
            for dot in row:
                if dot != 0:
                    total += 1
        return total


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    ori_paper = TransparentPaper()

    fold_flag = False
    for line in lines:
        if line == "":
            fold_flag = True
            continue

        if not fold_flag:
            ori_paper.add_dot(int(line.split(',')[0]), int(line.split(',')[1]))
        else:
            print(ori_paper.count_dots())
            fold_split = line.split(' ')[2].split('=')
            if fold_split[0] == 'y':
                ori_paper.fold_up(int(fold_split[1]))
            if fold_split[0] == 'x':
                ori_paper.fold_left(int(fold_split[1]))

    print(ori_paper.count_dots())
    print(ori_paper)