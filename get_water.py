def trap2(height):
    n = len(height)
    if n <= 2:
        return 0

    left, right = 0, n - 1  # 左右指针
    left_max, right_max = 0, 0  # 左右最高的柱子
    water = 0

    while left < right:
        # 确保了右边一定已经有了一个更高的柱子。
        if height[left] < height[right]:  # 处理左侧
            if height[left] >= left_max:
                left_max = height[left]  # 更新左侧最高
            else:
                water += left_max - height[left]  # 累加水量
            left += 1
        # 确保了左边一定有了一个更高的柱子。
        else:  # 处理右侧
            if height[right] >= right_max:
                right_max = height[right]  # 更新右侧最高
            else:
                water += right_max - height[right]  # 累加水量
            right -= 1

    return water

def trap(height):
    """
    :type height: List[int]
    :rtype: int

    这种算法，本质上还是一种局部的思维，你只考虑到了局部的情况，且该局部情况只有柱子高度连续增减的情况。
    同时是在考虑凹槽形成的一个整体。
    """
    water = 0
    l, r = 0, len(height) - 1
    while l < r:
        # Find container to store water.
        left, right = l-1, l+1
        if left < 0 or right > r: # Beyond left, right limit.
            l += 1
            continue
        if height[left] < height[l] or height[right] < height[l]:
            l += 1
            continue
        # Now, both left and right columns are heigher than current column, a container got
        # Find left-most column.
        while left > 0:
            if height[left-1] >= height[left]:
                left -= 1
                continue
            break
        # Find right-most column.
        while right < r:
            if height[right+1] >= height[right]:
                right += 1
                continue
            break

        print(left, right)

        ## Calculate water
        water += min(height[left], height[right]) * (right - left - 1)

        print('water: ', water)
        left += 1
        while left < right:
            water -= height[left]
            left += 1

        print('water refined: ', water)

        l = right + 1

    return water

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]

r1 = trap2(height1)
r2 = trap2(height2)

print(r1)
print(r2)
