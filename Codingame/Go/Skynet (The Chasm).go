package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
    jump := false

    // road: the length of the road before the gap.
    var road int
    fmt.Scan(&road)
    
    // gap: the length of the gap.
    var gap int
    fmt.Scan(&gap)
    
    // platform: the length of the landing platform.
    var platform int
    fmt.Scan(&platform)
    
    for {
        // speed: the motorbike's speed.
        var speed int
        fmt.Scan(&speed)
        
        // coordX: the position on the road of the motorbike.
        var coordX int
        fmt.Scan(&coordX)
        
        if jump == false {
            if coordX == road - 1 {
                jump = true
                fmt.Println("JUMP")
            } else if coordX < road - 1 {
                if speed < gap + 1 {
                    fmt.Println("SPEED")
                } else if speed > gap + 1 {
                    fmt.Println("SLOW")
                } else {
                    fmt.Println("WAIT")
                }
            }
        } else {
            fmt.Println("SLOW")
        }
        // fmt.Fprintln(os.Stderr, "Debug messages...")
        
        // A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    }
}