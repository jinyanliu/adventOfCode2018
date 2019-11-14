lineList = [line.rstrip('\n') for line in open('two')]
# print(lineList)


def process_string(string):
    has_twice = False
    has_triple = False
    counts_dict = {}
    for c in string:
        if c not in counts_dict.keys():
            counts_dict[c] = 1
        else:
            counts_dict[c] += 1
    # print(counts_dict)
    if 2 in counts_dict.values():
        has_twice = True
    if 3 in counts_dict.values():
        has_triple = True
    # print(has_twice, has_triple)
    return has_twice, has_triple


counts_twice = 0
counts_triple = 0
for string in lineList:
    a, b = process_string(string)
    if a:
        counts_twice += 1
    if b:
        counts_triple += 1
    print(a, b)
    print(counts_twice, counts_triple)
    print(counts_twice * counts_triple)

