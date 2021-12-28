def basin_size(y, x, hit_board, board):
    # searching outside bounds
    if (y < 0) or (y > len(board)-1) or (x < 0) or (x > len(board[0])-1):
        return 0
    # found 9 means terminate
    if board[y][x] == '9':
        hit_board[y][x] = 2
        return 0
    # found 1 means already explored (kill)
    if hit_board[y][x] == 1:
        return 0
    # found unexplored tile means add 1 to size and keep exploring
    if hit_board[y][x] == 0:
        hit_board[y][x] = 1
        return 1 + basin_size(y + 1, x, hit_board, board) \
                 + basin_size(y - 1, x, hit_board, board) \
                 + basin_size(y, x + 1, hit_board, board) \
                 + basin_size(y, x - 1, hit_board, board)


if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    sum_of_low_points = 0
    low_points_i = list()
    low_points_j = list()
    for i, row in enumerate(lines):
        for j, height in enumerate(row):
            islow = True

            if i != 0:
                if int(height) >= int(lines[i - 1][j]):
                    islow = False
            if i < (len(lines) - 1):
                if int(height) >= int(lines[i + 1][j]):
                    islow = False
            if j != 0:
                if int(height) >= int(row[j - 1]):
                    islow = False
            if j < (len(row) - 1):
                if int(height) >= int(row[j + 1]):
                    islow = False

            if islow:
                sum_of_low_points += int(height) + 1
                low_points_i.append(i)
                low_points_j.append(j)

    print(sum_of_low_points)

    basin_sizes = list()
    for index, i in enumerate(low_points_i):
        hit_matrix = [[0 for _ in lines[0]] for _ in lines]
        basin_sizes.append(basin_size(i, low_points_j[index], hit_matrix, lines))

    basin_sizes.sort()
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
