package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "strconv"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
    scanner := bufio.NewScanner(os.Stdin)

    // n: the number of temperatures to analyse
    res := 10000000
    rest := 0
    sent := false

    var n int
    scanner.Scan()
    fmt.Sscan(scanner.Text(),&n)
    
    scanner.Scan()
    temps := scanner.Text() // the n temperatures expressed as integers ranging from -273 to 5526
    arr := strings.Split(temps, " ")
    fmt.Fprintln(os.Stderr, arr)
    
    for _,value := range arr {
        val, _ := strconv.Atoi(value)
        if abs(val) < res {
            res = abs(val)
            rest = val
            if rest < 0 {
                sent = false
            } else {
                sent = true
            }
        } else if abs(val) == res && sent == false {
            rest = val
        } else if abs(val) == res && sent == true {
            rest = abs(val)
        } 
    }
    fmt.Println(rest)
}

func abs(num int) int {
    if num < 0 {
        return -1 * num
    }
    return num
}