
# LeetCode Problem Solving

Problem:

42. Trapping Rain Water 接雨水

description:

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 解题思路

1. 双指针解法
2. 单调栈解法

## 双指针解法

请用 Golang 实现，并给出测试用例

```go
func trap(height []int) int {
	left, right := 0, len(height) - 1
	leftMax, rightMax := 0, 0
	ans := 0
	for left < right {
		if height[left] < height[right] {
			if height[left] > leftMax {
				leftMax = height[left]
			} else {
				ans += leftMax - height[left]
			}
			left++
		} else {
			if height[right] > rightMax {
				rightMax = height[right]
			} else {
				ans += rightMax - height[right]
			}
		}
	}
	return ans
}
```

## 单调栈解法

请用 Golang 实现，并给出测试用例

```go
func trap(height []int) int {
	stack := []int{}
	ans := 0
	for i, h := range height {
		for len(stack) > 0 && height[stack[len(stack)-1]] < h {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				break
			}
			distance := i - stack[len(stack)-1] - 1
			boundedHeight := min(height[i], height[stack[len(stack)-1]]) - height[top]
			ans += distance * boundedHeight
		}
		stack = append(stack, i)
	}
	return ans
}
```

## 测试用例

```go
func TestTrap(t *testing.T) {
	cases := []struct {
		name string
		height []int
		want int
	}{
		{"case1", []int{0,1,0,2,1,0,1,3,2,1,2,1}, 6},
		{"case2", []int{4,2,0,3,2,5}, 9},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := trap(c.height)
			if got != c.want {
				t.Errorf("trap(%v) = %d; want %d", c.height, got, c.want)
			}
		})
	}
}
``` 

## 详细解题思路

Q1: 这个问题应该如何思考？

A1: 这个问题可以看作是求解一个柱子接雨水的问题。我们可以使用双指针解法和单调栈解法来解决这个问题。


Q2: 双指针解法和单调栈解法有什么区别？

A2: 双指针解法和单调栈解法都是基于贪心算法来解决这个问题的。双指针解法是从两端向中间遍历，而单调栈解法是从中间向两端遍历。

Q3: 双指针解法和单调栈解法的时间复杂度是多少？


### 双指针解法

1. 初始化两个指针 left 和 right，分别指向数组的两端。
2. 初始化两个变量 leftMax 和 rightMax，分别表示 left 和 right 指针左侧和右侧的最大高度。
3. 初始化一个变量 ans，表示接雨水的总量。
4. 使用一个 while 循环，当 left 小于 right 时，进行以下操作：
   - 如果 height[left] 小于 height[right]，则将 left 指针右移，并更新 leftMax。
   - 否则，将 right 指针左移，并更新 rightMax。
   - 如果 height[left] 大于 leftMax，则更新 leftMax。
   - 否则，将 ans 加上 leftMax 和 height[left] 的差值。
   - 如果 height[right] 大于 rightMax，则更新 rightMax。
   - 否则，将 ans 加上 rightMax 和 height[right] 的差值。
5. 返回 ans。

### 单调栈解法

1. 初始化一个栈 stack，用于存储柱子的索引。
2. 初始化一个变量 ans，表示接雨水的总量。
3. 使用一个 for 循环，遍历数组中的每个柱子：
   - 如果栈不为空且当前柱子的高度大于栈顶柱子的高度，则将栈顶柱子出栈，并计算接雨水的量。
   - 将当前柱子的索引入栈。
4. 返回 ans。

