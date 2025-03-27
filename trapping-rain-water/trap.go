package main

import "fmt"

// TrapWithTwoPointers solves the trapping rain water problem using two pointers approach
func TrapWithTwoPointers(height []int) int {
	left, right := 0, len(height)-1
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
			right--
		}
	}
	return ans
}

// TrapWithStack solves the trapping rain water problem using monotonic stack approach
func TrapWithStack(height []int) int {
	stack := []int{} // 单调栈, 存储柱子的索引
	ans := 0         // 接雨水的总量
	for i, h := range height {
		fmt.Println("i", i, "h", h)
		for len(stack) > 0 && height[stack[len(stack)-1]] < h {
			stack_head := len(stack) - 1 // 栈顶元素的索引
			top := stack[stack_head]     // 栈顶元素的值
			stack = stack[:stack_head]   // 弹出栈顶元素
			fmt.Println("inner top", top, "inner stack", stack)
			if len(stack) == 0 {
				break
			}
			distance := i - stack[stack_head] - 1                                    // 计算距离
			boundedHeight := min(height[i], height[stack[stack_head]]) - height[top] // 计算接雨水的量
			ans += distance * boundedHeight                                          // 累加接雨水的量
			fmt.Println("distance", distance, "boundedHeight", boundedHeight, "ans", ans)
		}
		stack = append(stack, i) // 将当前柱子的索引入栈
		fmt.Println("stack", stack)
	}
	return ans // 返回接雨水的总量
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
