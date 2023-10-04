package main

import "fmt"

func bubble_sort(arr []int) []int {
	var temp int
	var length int
	length = len(arr)
	for i := 0; i < length; i++ {
		for j := 0; j < length-i-1; j++ {
			if arr[j] > arr[j+1] {
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
			}
		}
	}
	return arr
}

func main() {
	var x int
	fmt.Println("Input size")
	fmt.Scan(&x)
	fmt.Println("Input array")
	arr := make([]int, x)
	for i := 0; i < x; i++ {
		fmt.Println("Next number")
		fmt.Scan(&arr[i])
	}
	arr = bubble_sort(arr)
	fmt.Println(arr)
}
