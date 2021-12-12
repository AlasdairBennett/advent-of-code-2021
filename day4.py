class BingoBoard:
    board = [[]]
    hit_board = [[]]

    def __init__(self, brd):
        self.board = brd
        self.hit_board = [[0 for _ in brd[0]] for _ in brd]

    def check_num(self, num):
        for i, row in enumerate(self.board):
            for j, item in enumerate(row):
                if item == num:
                    self.hit_board[i][j] = 1

    def check_win(self):
        for row in self.hit_board:
            winflag = len(row)
            for elem in row:
                if elem == 1:
                    winflag -= 1
            if winflag == 0:
                return True
        # check columns
        for i, e in enumerate(self.board[0]):
            winflag = len(self.hit_board[0])
            for row in self.hit_board:
                if row[i] == 1:
                    winflag -= 1
            if winflag == 0:
                return True

        return False

    def get_score(self, latest):
        score = 0

        for i, row in enumerate(self.hit_board):
            for j, item in enumerate(row):
                if item == 0:
                    score += self.board[i][j]

        score = score * latest
        return score

    def __repr__(self):
        r = ""
        for borl in self.board:
            r += str(borl)
            r += "\n"
        r += "\n"
        for hit in self.hit_board:
            r += str(hit)
            r += "\n"
        r += "\n"
        return r


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    drawList = list(map(int, lines[0].split(",")))
    lines.remove(lines[0])

    bboards = []

    for line in lines:
        if line == "":
            bboards.append([])
            continue
        splitline = line.split(" ")
        splitline = list(filter("".__ne__, splitline))
        bboards[len(bboards) - 1].append(list(map(int, splitline)))

    boards = []
    for board in bboards:
        boards.append(BingoBoard(board))


    flag = 0
    for n in drawList:
        if flag == 1:
            break
        for board in boards:
            # print(board)
            if flag == 1:
                break
            board.check_num(n)
            if board.check_win():
                print(board.get_score(n))
                flag = 1

    score_arr = []
    board_wins = [0 for _ in boards]
    for n in drawList:
        for i, board in enumerate(boards):
            if board_wins[i] == 1:
                continue
            board.check_num(n)
            if board.check_win():
                board_wins[i] = 1
                score_arr.append(board.get_score(n))
    print(score_arr)
    print(score_arr[len(score_arr) - 1])
