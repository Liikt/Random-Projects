package main

import "fmt"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

func main() {
    // lightX: the X position of the light of power
    // lightY: the Y position of the light of power
    // initialTX: Thor's starting X position
    // initialTY: Thor's starting Y position
    var lightX, lightY, initialTX, initialTY int
    fmt.Scan(&lightX, &lightY, &initialTX, &initialTY)
    
    for {
        // remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
        var remainingTurns int
        var erg string
        fmt.Scan(&remainingTurns)
        
        
        // fmt.Fprintln(os.Stderr, "Debug messages...")
        
        // A single line providing the move to be made: N NE E SE S SW W or NW
        if initialTY < 18 && initialTY >= 0 {
            if lightY > initialTY {
                erg += "S"
                initialTY++
            } else if lightY < initialTY {
                erg += "N"
                initialTY--
            }
        }

        if initialTX < 40 && initialTX >= 0 {
            if lightX > initialTX {
                erg += "E"
                initialTX++
            } else if lightX < initialTX {
                erg += "W"
                initialTX--
            }
        }

        fmt.Println(erg)
    }
}