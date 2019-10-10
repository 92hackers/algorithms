# Leet Code
# 一个贼，去别人家偷东西，不能偷连续的两家，否则会报警，
# 每家能偷的金额已经知道了，选择偷哪几家能够最大化收益？

def rob(nums):
    now = 0
    last = 0

    for n in nums:
        temp = now
        now = max(now, last + n)
        last = temp

    return now


if __name__ == '__main__':
    houses = [1, 34, 56, 1, 26, 99, 100, 200, 1, 2, 98]
    print(rob(houses))
