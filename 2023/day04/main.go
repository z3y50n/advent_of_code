package main

import (
	"aoc/2023/utils"
	"fmt"
	"math"
	"strings"
)

func part1(cards []string) int {
	var points int

	for _, card := range cards {
		var matches int
		numbers := strings.Split(strings.Split(card, ":")[1], "|")

		winningNumbers := strings.Fields(numbers[0])
		ownNumbers := strings.Fields(numbers[1])

		for _, n := range ownNumbers {
			if utils.ContainsString(winningNumbers, n) {
				matches++
			}
		}
		points += int(math.Pow(2, float64(matches-1)))
	}

	return points
}

func part2(cards []string) int {
	cardsMap := make(map[int]int)
	for i := range cards {
		cardsMap[i+1] = 1
	}

	for i, card := range cards {
		var matches int
		numbers := strings.Split(strings.Split(card, ":")[1], "|")

		winningNumbers := strings.Fields(numbers[0])
		ownNumbers := strings.Fields(numbers[1])

		for _, n := range ownNumbers {
			if utils.ContainsString(winningNumbers, n) {
				matches++
			}
		}
		for j := 1; j <= matches; j++ {
			cardsMap[i+1+j] += cardsMap[i+1]
		}
	}
	var points int
	for _, v := range cardsMap {
		points += v
	}
	return points
}

func main() {
	test_cards := utils.ReadS("test_data.txt")
	cards := utils.ReadS("data.txt")

	res_1t := part1(test_cards)
	if res_1t != 13 {
		fmt.Println("Error in part 1. Got", res_1t)
		return
	}
	res1 := part1(cards)
	fmt.Println("Part 1:", res1)

	res_2t := part2(test_cards)
	if res_2t != 30 {
		fmt.Println("Error in part 2. Got", res_2t)
		return
	}
	res2 := part2(cards)
	fmt.Println("Part 2:", res2)
}
