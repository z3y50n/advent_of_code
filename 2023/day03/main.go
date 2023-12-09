package main

import (
	"aoc/2023/utils"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
	"unicode"
)

func isPart(i, j, n int, engine []string) bool {
	if n == 0 {
		return false
	}
	N := len(engine)

	for k := i - 1; k <= i+1; k++ {
		for l := j - 1 - n; l <= j; l++ {
			if k == -1 || k == N || l == -1 {
				continue
			}
			if engine[k][l] != '.' && !unicode.IsNumber(rune(engine[k][l])) {
				return true
			}
		}
	}
	return false
}

func Part1(engine []string) int {
	var sum int

	for i, line := range engine {
		var num []string
		for j, c := range line {
			if unicode.IsNumber(c) {
				num = append(num, string(c))
			}
			if !unicode.IsNumber(c) || j == len(line)-1 {
				if isPart(i, j, len(num), engine) {
					n, err := strconv.Atoi(strings.Join(num, ""))
					if err != nil {
						fmt.Println(err)
						os.Exit(1)
					}
					sum += n
				}
				num = nil
			}
		}
	}
	return sum
}

func getRatio(i, j int, engine []string) int {
	re := regexp.MustCompile(`(\d+)`)
	nums := []string{}
	for l := i - 1; l <= i+1; l++ {
		if l == -1 || l == len(engine) {
			continue
		}
		matches := re.FindAllStringIndex(engine[l], -1)
		numbers := re.FindAllString(engine[l], -1)
		for k, match := range matches {
			start := match[0]
			end := match[1]
			if (j-1 <= start && start <= j+1) || (j-1 <= end-1 && end-1 <= j+1) {
				nums = append(nums, numbers[k])
			}
		}

	}

	if len(nums) == 2 {
		n1, _ := strconv.Atoi(nums[0])
		n2, _ := strconv.Atoi(nums[1])
		return n1 * n2
	}

	return -1
}

func Part2(engine []string) int {
	var sum int
	for i, line := range engine {
		for j, c := range line {
			if c == '*' {
				gearRatio := getRatio(i, j, engine)
				if gearRatio != -1 {
					sum += gearRatio
				}
			}
		}
	}

	return sum
}

func main() {
	test_engine := utils.ReadS("test_data.txt")
	engine := utils.ReadS("data.txt")

	res_1t := Part1(test_engine)
	if res_1t != 4361 {
		fmt.Println("Part 1 error")
		return
	}

	res1 := Part1(engine)
	fmt.Println("Part 1:", res1)

	res_t2 := Part2(test_engine)
	if res_t2 != 467835 {
		fmt.Println("Part 2 error")
		return
	}

	res2 := Part2(engine)
	fmt.Println("Part 2:", res2)
}
