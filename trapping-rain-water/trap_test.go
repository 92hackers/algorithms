package main

import (
	"testing"
)

func TestTrapWithTwoPointers(t *testing.T) {
	cases := []struct {
		name   string
		height []int
		want   int
	}{
		{"case1", []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}, 6},
		{"case2", []int{4, 2, 0, 3, 2, 5}, 9},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := TrapWithTwoPointers(c.height)
			if got != c.want {
				t.Errorf("TrapWithTwoPointers(%v) = %d; want %d", c.height, got, c.want)
			}
		})
	}
}

func TestTrapWithStack(t *testing.T) {
	cases := []struct {
		name   string
		height []int
		want   int
	}{
		{"case1", []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}, 6},
		{"case2", []int{4, 2, 0, 3, 2, 5}, 9},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := TrapWithStack(c.height)
			if got != c.want {
				t.Errorf("TrapWithStack(%v) = %d; want %d", c.height, got, c.want)
			}
		})
	}
}
