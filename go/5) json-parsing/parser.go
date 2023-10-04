package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	ID   int    `json:"id"`
	NAME string `json:"name"`
	AGE  int    `json:"age"`
}

func encode_json(id int, name string, age int) string {
	person := Person{ID: id, NAME: name, AGE: age}
	item, error := json.Marshal(person)
	if error != nil {
		panic(error)
	}
	return string(item)
}

func decode_json(json_data string) {
	byt := []byte(json_data)
	var data map[string]interface{}

	if err := json.Unmarshal(byt, &data); err != nil {
		panic(err)
	}
	fmt.Println(data)
}

func main() {
	var choice int
	fmt.Println("Encode or decode? 1/2")
	fmt.Scan(&choice)

	if choice == 1 {
		var id int
		var name_person string
		var age int

		fmt.Println("id:")
		fmt.Scan(&id)
		fmt.Println("name:")
		fmt.Scan(&name_person)
		fmt.Println("age:")
		fmt.Scan(&age)
		json_data := encode_json(id, name_person, age)
		fmt.Printf("%s", json_data)
	}

	if choice == 2 {
		var name string
		fmt.Println("Input json name")
		fmt.Scan(&name)
		file := name + ".json"
		data, error := os.ReadFile(file)

		if error != nil {
			panic(error)
		}
		decode_json(string(data))

	}
	return
}
