if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))

    syntax_error_total = 0
    total_scores = []
    for i, line in enumerate(lines):

        bracket_stack = []
        corrupted_flag = False
        for synchar in line:
            if synchar in '([{<':
                bracket_stack.append(synchar)

            if synchar == ')':
                if bracket_stack.pop() != '(':
                    corrupted_flag = True
                    syntax_error_total += 3
                    break

            if synchar == ']':
                if bracket_stack.pop() != '[':
                    corrupted_flag = True
                    syntax_error_total += 57
                    break

            if synchar == '}':
                if bracket_stack.pop() != '{':
                    corrupted_flag = True
                    syntax_error_total += 1197
                    break

            if synchar == '>':
                if bracket_stack.pop() != '<':
                    corrupted_flag = True
                    syntax_error_total += 25137
                    break
        if not corrupted_flag:
            total_score = 0
            for br in reversed(bracket_stack):
                total_score *= 5
                if br == '(':
                    total_score += 1
                if br == '[':
                    total_score += 2
                if br == '{':
                    total_score += 3
                if br == '<':
                    total_score += 4
            total_scores.append(total_score)

    print(syntax_error_total)

    total_scores.sort()
    print(total_scores[len(total_scores) // 2])
