package main

import (
	"fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func read(filename string) []int{
    n, _ := ioutil.ReadFile(filename)
    s := strings.Trim(string(n), "\n")
    inputs := strings.Split(s, "\n")

    numbers := []int{}
    for _, i := range inputs{
        num, _ := strconv.Atoi(i)
        numbers = append(numbers, num)
    }
    return numbers
}

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
    data := read("day1a.txt")
    fmt.Println(part1(data))
    fmt.Println(part2(data))
}
