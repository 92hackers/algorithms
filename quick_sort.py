# 快速排序
# From 算法导论，非常精妙的一个实现

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# 执行子数组的二分排序，
# 默认数组里面全部是大于目标数的，
# 通过挪动小于目标数的 section 的指针，交换新遇到的小数
# 非常精妙，简洁的算法
#
# 此处用了随机选择目标数
def partition(arr, i, j):
    target = random.randint(i, j)
    swap(arr, target, j)

    # left pointer
    x = i - 1

    for y in range(i, j):
        if arr[y] <= arr[j]:
            x += 1
            swap(arr, x, y)

    swap(arr, x + 1, j)

    return x + 1
    

def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        #  return

        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)

sample = [52, 2, 14, 9, 34, 99, 4, 8, 10, 11, 1, 0, 3, 7, 5, 43, 78, 67]
print('before: ', sample)

quick_sort(sample, 0, len(sample) - 1)

print('After: ', sample)
