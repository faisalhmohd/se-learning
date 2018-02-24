package main

import (
    "fmt"
    "bufio"
    "os"
)

func main(){
    reader := bufio.NewReader(os.Stdin)
    sentence, _ := reader.ReadString('\n')

    fmt.Println("Hello, World.")
    fmt.Println(sentence)   
}