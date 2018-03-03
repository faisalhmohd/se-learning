package main
import (
  "fmt"
  "bufio"
  "os"
  "strconv"
)

func main() {
  //Enter your code here. Read input from STDIN. Print output to STDOUT
  scanner := bufio.NewScanner(os.Stdin)
  var tmp string

  for scanner.Scan() {
    tmp = scanner.Text()
    tmpint, _ := strconv.ParseInt(tmp, 10, 64)
    if tmpint%2 != 0 {
      fmt.Println("Weird")
    } else if tmpint >= 2 && tmpint <= 5 {
      fmt.Println("Not Weird")
    } else if tmpint >= 6 && tmpint <= 20 {
      fmt.Println("Weird")
    } else {
      fmt.Println("Not Weird")
    }  
  }
}
