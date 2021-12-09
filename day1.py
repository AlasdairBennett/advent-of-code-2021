def scan_file(filename):
    fo = open(filename)
    return fo.readlines();


def depth_increase_count(depths):
    increase = 0
    prev_depth = depths[0]
    for depth in depths:
        if depth > prev_depth:
            increase += 1
        prev_depth = depth
    return increase


def sliding_window_depth_increase_count(depths):
    increase = 0
    prev_sum = float('inf')
    for i, depth in enumerate(depths):
        if i+2 >= len(depths):
            break
        dsum = depths[i] + depths[i+1] + depths[i+2]
        if dsum > prev_sum:
            increase += 1
        prev_sum = dsum
    return increase


if __name__ == '__main__':
    int_depths = [int(n) for n in scan_file("input.txt")]
    print(depth_increase_count(int_depths))
    print(sliding_window_depth_increase_count(int_depths))
