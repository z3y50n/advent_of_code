package main

import (
    "fmt"
    "advent-of-code/tools"
    "math"
    "sort"
)

// Find Median
func part1(numbers []int) int {
    nums := make([]int, len(numbers))
    copy(nums, numbers)
    sort.Ints(nums)
    median := nums[len(nums) / 2]

    fuel := 0
    for _, n := range nums {
        fuel += int(math.Abs(float64(n - median)))
    }
    return fuel
}

func part2(numbers []int) int {
    left := tools.Min(numbers)
    right := tools.Max(numbers)
    var fuels []int
    for i := left; i <= right; i++ {
        fuel := 0
        for _, n := range numbers {
            diff := int(math.Abs(float64(n - i)))
            fuel += ar_prog(diff)
        }
        fuels = append(fuels, fuel)
    }
    return tools.Min(fuels)
}

// Arithmetic Progression sum
func ar_prog(x int) int {
    return x * (x + 1) / 2
}

func main() {
    numbers := tools.Read("input.txt", ",")
    fmt.Println(part1(numbers))
    fmt.Println(part2(numbers))

}
