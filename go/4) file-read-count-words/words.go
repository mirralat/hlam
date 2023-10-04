package main

import (
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func unique_words_count(arr []string) []string {
	var uniqueArray []string
	var flag bool
	for v := range arr {
		flag = true
		if len(uniqueArray) > 1 {
			for u := range uniqueArray {
				fmt.Println(uniqueArray[u])
				if arr[v] == uniqueArray[u] {
					flag = false
					break
				}
			}
			if flag {
				uniqueArray = append(uniqueArray, arr[v])
			}
		}
		if len(uniqueArray) <= 1 {
			uniqueArray = append(uniqueArray, arr[v])
		}
	}
	return uniqueArray
}

func main() {
	data, error := os.ReadFile("text.txt")
	check(error)
	array := unique_words_count(strings.Split(string(data), "\n"))
	fmt.Println("New")
	fmt.Println(array)
}
