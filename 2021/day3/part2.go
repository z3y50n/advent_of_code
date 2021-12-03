package main

import (
    "strconv"
)

func part2(input []string) int {
    tmp := make([]string, len(input))
    copy(tmp, input)
    ox_rating := extract(tmp, 0)
    tmp = make([]string, len(input))
    copy(tmp, input)
    co2_rating := extract(tmp, 1)

    ox, _ := strconv.ParseInt(ox_rating, 2, 64)
    co2, _ := strconv.ParseInt(co2_rating, 2, 64)

    return int(ox * co2)
}

func extract(rating []string, mask int) string {
    idx := 0
    for len(rating) > 1 {
        var temp []string
        // Count bits
        ones := 0
        zeros := 0
        for _, val := range rating {
            if val[idx] == '1' {
                ones++
            } else {
                zeros++
            }
        }
        bit := det_bit(ones, zeros, mask)

        for _, val := range rating {
            if string(val[idx]) == bit {
                temp = append(temp, val)
            }
        }
        idx++
        rating = make([]string, len(temp))
        copy(rating, temp)
    }
    return rating[0] 
}

func det_bit(ones, zeros, mask int) string {
    var bit string
    if ones > zeros {
        if mask == 0 {
            bit = "1"
        } else {
            bit = "0"
        }
    } else if ones < zeros {
        if mask == 0 {
            bit = "0"
        } else {
            bit = "1"
        }
    } else {
        if mask == 0 {
            bit = "1"
        } else {
            bit = "0"
        }
    }
    return bit
}
