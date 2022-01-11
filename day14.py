from collections import Counter

if __name__ == '__main__':
    fo = open("input.txt")
    lines = fo.readlines()
    lines = list(map(str.strip, lines))
    lines = [_.replace(" ", "") for _ in lines]

    polymer_template = lines[0]

    insertion_rules = []
    for line in lines[2:]:
        insertion_rules.append(line.split("->"))

    for step_count in range(40):
        next_polymer_template = ""
        for i, elem in enumerate(polymer_template[:-1]):
            next_polymer_template += elem
            pair = elem + polymer_template[i+1]
            for rule in insertion_rules:
                if rule[0] == pair:
                    next_polymer_template += rule[1]
        next_polymer_template += polymer_template[-1]
        polymer_template = next_polymer_template

    freq = Counter(polymer_template).most_common()
    print(str(freq[0][1] - freq[-1][1]))
