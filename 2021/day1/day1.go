package main

import (
	"fmt"
    "advent-of-code/tools"
)

func part1(data []int) int{
    inc := 0
    for i := 1; i < len(data); i++{
        if data[i] > data[i-1]{
            inc++
        }
    }
    return inc
}

func part2(data []int) int{
    inc := 0
    for i:=1; i < len(data)-2; i++{
        m1 := data[i-1] + data[i] + data[i+1]
        m2 := data[i] + data[i+1] + data[i+2]
        if m2 > m1{
            inc ++
        }
    }
    return inc

}

func main() {
    data := tools.Read("day1a.txt")
    fmt.Println(part1(data))
    fmt.Println(part2(data))
}
