# Flexport onsite interview question
# 以楔形的排列方式，排列数组里面的所有元素，同时，从第一层开始，将最终
# 结果输出出来

def getIndexLoop(loop):
    return [i for i in range(1, loop)] + [j for j in range(loop, 0, -1)]

def alignItemsInWedgeShape(arr):
    results = [[] for x in range(int(len(arr) / 2))]

    loop = 2
    new_arr = list(reversed(arr))
    index_loop_arr = getIndexLoop(loop)

    while new_arr:
        target_index = index_loop_arr.pop()
        char = new_arr.pop()

        results[target_index].append(char)

        if not index_loop_arr:
            loop += 2
            index_loop_arr = getIndexLoop(loop)

    for i in results:
        if i:
            print(i)

arr = [i for i in range(1, 60)]

alignItemsInWedgeShape(arr)
