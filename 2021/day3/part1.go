package main

import (
	"strconv"
	"strings"
)

func part1(input []string) int {
    size := len(input[0])
    var gamma strings.Builder
    var epsilon strings.Builder
    for i := 0; i < size; i++ {
        ones := 0
        zeros := 0
        for _, m := range input {
            if m[i] == '1' {
                ones++
            } else {
                zeros++
            }

        }
        if ones > zeros {
            gamma.WriteString("1")
            epsilon.WriteString("0")
        } else {
            gamma.WriteString("0")
            epsilon.WriteString("1")
        }
    }
    g, _ := strconv.ParseInt(gamma.String(), 2, 64)
    e, _ := strconv.ParseInt(epsilon.String(), 2, 64)
    return int(g * e)
}
