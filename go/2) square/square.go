package main

import 
(
"fmt"
)


func square_area(x int, y int) int{
	var z int
	z = x * y
	return z 
}

func main(){
	var x, y, z int
	fmt.Println("Input x");
	fmt.Scan(&x)
	fmt.Println("Input y")
	fmt.Scan(&y)
	z = square_area(x, y)
	fmt.Println(z)
}