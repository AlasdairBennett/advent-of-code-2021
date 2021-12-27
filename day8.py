if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    signal_patterns = []
    output_patterns = []

    for i, line in enumerate(lines):
        signal_patterns.append(list(map(str.strip, line.split("|")))[0].split(" "))
        output_patterns.append(list(map(str.strip, line.split("|")))[1].split(" "))

    # part 1
    digit1 = 0
    digit4 = 0
    digit7 = 0
    digit8 = 0

    for pattern in output_patterns:
        for segment in pattern:
            if len(segment) == 2:
                digit1 += 1
            elif len(segment) == 4:
                digit4 += 1
            elif len(segment) == 3:
                digit7 += 1
            elif len(segment) == 7:
                digit8 += 1

    print(str(digit1 + digit4 + digit7 + digit8))

    # part 2
    output_total = 0
    for rowIndex, pattern in enumerate(signal_patterns):
        # one line of input at a time
        char_lookup_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        char_conversion_arr = [''] * 7
        line_count_arr = [0] * 7
        one_seg = ""
        four_seg = ""
        for segment in pattern:
            # one of the 10 unique signal patterns
            if len(segment) == 2:
                one_seg = segment
            if len(segment) == 4:
                four_seg = segment
            if 'a' in segment:
                line_count_arr[0] += segment.count('a')
            if 'b' in segment:
                line_count_arr[1] += segment.count('b')
            if 'c' in segment:
                line_count_arr[2] += segment.count('c')
            if 'd' in segment:
                line_count_arr[3] += segment.count('d')
            if 'e' in segment:
                line_count_arr[4] += segment.count('e')
            if 'f' in segment:
                line_count_arr[5] += segment.count('f')
            if 'g' in segment:
                line_count_arr[6] += segment.count('g')

        for i, char_count in enumerate(line_count_arr):
            if char_count == 9:
                char_conversion_arr[i] = 'f'
            if char_count == 6:
                char_conversion_arr[i] = 'b'
            if char_count == 4:
                char_conversion_arr[i] = 'e'

            if char_count == 8:
                if char_lookup_arr[i] in one_seg:
                    char_conversion_arr[i] = 'c'
                else:
                    char_conversion_arr[i] = 'a'

            if char_count == 7:
                if char_lookup_arr[i] in four_seg:
                    char_conversion_arr[i] = 'd'
                else:
                    char_conversion_arr[i] = 'g'

        # decode output line and add it
        line_total = ""
        for i, outseg in enumerate(output_patterns[rowIndex]):
            newSeg = ""

            for outsegchar in outseg:
                newSeg += char_conversion_arr[ord(outsegchar) - 97]

            newSeg = "".join(sorted(newSeg))
            if newSeg == "cf":
                line_total += "1"
            if newSeg == "acdeg":
                line_total += "2"
            if newSeg == "acdfg":
                line_total += "3"
            if newSeg == "bcdf":
                line_total += "4"
            if newSeg == "abdfg":
                line_total += "5"
            if newSeg == "abdefg":
                line_total += "6"
            if newSeg == "acf":
                line_total += "7"
            if newSeg == "abcdefg":
                line_total += "8"
            if newSeg == "abcdfg":
                line_total += "9"
            if newSeg == "abcefg":
                line_total += "0"

        if len(line_total) == 4:
            output_total += int(line_total)
        else:
            print("We fucked up!!! " + str(rowIndex) + ", " + line_total)
    print(output_total)
