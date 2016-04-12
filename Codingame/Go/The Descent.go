package main

import "fmt"
import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
    for {
        mnt := make([]int, 8)
        for i := 0; i < 8; i++ {
            // mountainH: represents the height of one mountain, from 9 to 0       
            fmt.Scan(&mnt[i])
        }

        max := 0
        ind := 0
        for index,value := range mnt {
        if max < value {
            max = value
            ind = index
            fmt.Fprintln(os.Stderr, ind)
        }
    }
        fmt.Println(ind) // The number of the mountain to fire on.
    }
}