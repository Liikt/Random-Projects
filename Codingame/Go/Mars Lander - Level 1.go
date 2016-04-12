package main

import "fmt"
import "math"
//import "os"

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {
    // surfaceN: the number of points used to draw the surface of Mars.
    var surfaceN int
    fmt.Scan(&surfaceN)
    var landX, landY int

    maxv := 40.0
    g := 3.711
    a := g-4
    step := 0
    
    for i := 0; i < surfaceN; i++ {
        // landX: X coordinate of a surface point. (0 to 6999)
        // landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        fmt.Scan(&landX, &landY)
    }
    for {
        // hSpeed: the horizontal speed (in m/s), can be negative.
        // vSpeed: the vertical speed (in m/s), can be negative.
        // fuel: the quantity of remaining fuel in liters.
        // rotate: the rotation angle in degrees (-90 to 90).
        // power: the thrust power (0 to 4).
        var X, Y, hSpeed, vSpeed, fuel, rotate, power int
        fmt.Scan(&X, &Y, &hSpeed, &vSpeed, &fuel, &rotate, &power)
        
        
        // fmt.Fprintln(os.Stderr, "Debug messages...")
        
        // 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).

        step++
        if step % 8 == 0 {
            fmt.Println("0 4")
        } else {
            D := math.Pow(float64(vSpeed),2) + 2.0*a*float64(Y)
            if D >= 0 && math.Pow(float64(D), 0.5) >= maxv - (1+2+3+4) {
                fmt.Println("0 4")
            } else {
                fmt.Println("0 0")
            }
        }
    }
}