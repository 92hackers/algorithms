# Flexport onsite interview question
# Given below dict input
# { 'a': [1, 2, 3], 'b': [8, 9, 11], 'c': [0, 4, 5] }
#
# Given string input: 'ab', to find all combinations
# ['18', '19', '111', '28', '29', '211', '38', '39', '311']
#
# DP-like algorithm, calculate out evary results, and accumlate up.

def stringMerge(dict_data, string):
    result = []
    temp_result = []

    for char in string:
        temp_result = []
        target_list = dict_data[char]

        if not result:
            result = target_list
            continue

        for item in result:
            temp_result += [item + i for i in target_list]

        result = temp_result

    return result


dictData = {
    'a': ['1', '2', '3'],
    'b': ['4', '5', '6'],
    'c': ['7', '8', '9'],
    'd': ['10', '11', '12'],
}

tempString = 'acb'

print(stringMerge(dictData, tempString))
