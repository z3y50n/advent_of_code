package tools

import (
    "io/ioutil"
    "strings"
    "strconv"
)

func Read(filename string) []int{
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
