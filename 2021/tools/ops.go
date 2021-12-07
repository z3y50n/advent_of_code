package tools

func Min(numbers []int) int {
    var m int
    for i, n := range numbers {
        if i==0 || n < m {
            m = n
        }
    }
    return m
}

func Max(numbers []int) int {
    var m int
    for i, n := range numbers {
        if i==0 || n > m {
            m = n
        }
    }
    return m
}

func Sum(numbers []int) int {
    s := 0
    for _, n := range numbers {
        s += n
    }
    return s
}
