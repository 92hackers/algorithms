# "cyiaewdhnunsmrhlooleastlr"
# 1    1
# 2   22
# 3  3 3  3
# 4 4  4 4
# 5    5
#

import re
import itertools

def convert(s, numRows):
    if not s or numRows < 2 or numRows >= len(s):
        return s

    result = ''
    loop = 1
    count = 0
    current_index = 1

    rows = ['' for x in range(numRows)]

    group_map = {}

    cycle_up = range(0, numRows-1)
    cycle_down = range(numRows-1, 0, -1)
    iterator = itertools.cycle(list(cycle_up) + list(cycle_down))

    result = [""] * numRows
    for char in s:
        result[next(iterator)] += char

    print(list(cycle_up))
    print(list(cycle_down))
    print(result)

    return "".join(result)

    # Above code is the most efficient algorithm

    for c in s:
        if current_index in group_map:
            group_map[current_index] += c
        else:
            group_map[current_index] = c

        rows[current_index - 1] += c

        count += 1

        if count == numRows:
            count = 1
            if current_index == numRows:
                loop = 0
            elif current_index == 1:
                loop = 1

        if loop:
            current_index += 1
        else:
            current_index -= 1

    print(rows)
    print(''.join(rows))

    for i in range(1, numRows + 1):
        result += group_map[i]

    return result

sample = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."

# output should be:  "cyiaewdhnunsmrhlooleastlr"
numRows = 10

print(convert(sample, numRows))
