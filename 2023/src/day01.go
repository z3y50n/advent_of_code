package main

import (
	"aoc/2023/utils"
	"fmt"
	"strings"
	"unicode"
)

var numbers = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func part1(lines []string) int {
	var sum int = 0
	for _, line := range lines {
		var first int = -1
		var last int
		for _, c := range line {
			if unicode.IsNumber(c) {
				digit := int(c - '0')
				if first == -1 {
					first = digit
				}
				last = digit
			}
		}
		sum += first*10 + last
	}
	return sum
}

func part2(lines []string) int {
	var sum int = 0
	for _, line := range lines {
		var first int = -1
		var last int
		for i, c := range line {
			if unicode.IsNumber(c) {
				digit := int(c - '0')
				if first == -1 {
					first = digit
				}
				last = digit
			} else {
				for k, v := range numbers {
					if strings.HasPrefix(line[i:], k) {
						if first == -1 {
							first = v
						}
						last = v
					}

				}
			}
		}
		sum += first*10 + last
	}
	return sum
}

func main() {
	test_lines1 := utils.ReadS("data/01_test.txt")
	test_lines2 := utils.ReadS("data/01_test2.txt")
	lines := utils.ReadS("data/01.txt")

	// Part 1
	res1t := part1(test_lines1)
	if res1t != 142 {
		fmt.Println("Error in part 1. Expected 142, got", res1t)
		return
	}
	res1 := part1(lines)
	fmt.Println(res1)

	// Part 2
	res2t := part2(test_lines2)
	if res2t != 281 {
		fmt.Println("Error in part 2. Expected 281, got", res2t)
		return
	}
	res2 := part2(lines)
	fmt.Println(res2)
}
