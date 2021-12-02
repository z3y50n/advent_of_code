package main

import (
	"advent-of-code/tools"
	"fmt"
	"strconv"
	"strings"
)

func part1(course []string) int {
    pos := []int{0, 0}
    for _, cmd := range course {
        move := strings.Split(cmd, " ")
        d := move[0]
        u, _ := strconv.Atoi(move[1])

        if d == "forward" {
            pos[0] += u
        } else if d == "down"{
            pos[1] += u
        } else {
            pos[1] -= u
        }

    }
    return pos[0] * pos[1]
}

func part2(course []string) int {
    var aim int = 0
    pos := []int{0, 0}
    for _, cmd := range course {
        move := strings.Split(cmd, " ")
        d := move[0]
        u, _ := strconv.Atoi(move[1])

        if d == "forward" {
            pos[0] += u
            pos[1] += aim * u
        } else if d == "down"{
            aim += u
        } else {
            aim -= u
        }

    }
    return pos[0] * pos[1]
}

func main() {
    input := tools.ReadS("day2.txt")
    fmt.Println(part1(input))
    fmt.Println(part2(input))
}
