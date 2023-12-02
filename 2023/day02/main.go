package main

import (
	"aoc/2023/utils"
	"fmt"
	"strconv"
	"strings"
)

var colors = map[string]int{
	"red":   12,
	"green": 13,
	"blue":  14,
}

func part1(games []string) int {
	sum := 0
	for id, game := range games {
		start := strings.Index(game, ":") + 2
		rounds := strings.Split(game[start:], ";")
		isValid := true
		for _, round := range rounds {
			if !isValid {
				break
			}
			cubes := strings.Split(round, ",")
			for _, cube := range cubes {
				x := strings.Split(strings.Trim(cube, " "), " ")
				num, _ := strconv.Atoi(x[0])
				color := x[1]
				if num > colors[color] {
					isValid = false
					break
				}
			}
		}
		if isValid {
			sum += id + 1
		}
	}
	return sum
}

func part2(games []string) int {
	sum := 0
	for _, game := range games {
		start := strings.Index(game, ":") + 2
		rounds := strings.Split(game[start:], ";")
		var maxes = map[string]int{"red": 0, "blue": 0, "green": 0}

		for _, round := range rounds {
			cubes := strings.Split(round, ",")
			for _, cube := range cubes {
				x := strings.Split(strings.Trim(cube, " "), " ")
				num, _ := strconv.Atoi(x[0])
				color := x[1]
				if num > maxes[color] {
					maxes[color] = num
				}
			}
		}
		sum += maxes["red"] * maxes["blue"] * maxes["green"]
	}
	return sum
}

func main() {
	test_games := utils.ReadS("test_data.txt")
	games := utils.ReadS("data.txt")

	res1t := part1(test_games)
	if res1t != 8 {
		fmt.Println("Error in part 1. Got", res1t)
		return
	}

	res1 := part1(games)
	fmt.Println("Part1:", res1)

	res2t := part2(test_games)
	if res2t != 2286 {
		fmt.Println("Error in part 2. Got", res2t)
		return
	}

	res2 := part2(games)
	fmt.Println("Part2:", res2)
}
