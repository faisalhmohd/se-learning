package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
)

func main() {
  var _ = strconv.Itoa // Ignore this comment. You can still use the package "strconv".

  var i uint64 = 4
  var d float64 = 4.0
  var s string = "HackerRank "

  scanner := bufio.NewScanner(os.Stdin)

  // Declare second integer, double, and String variables.
  var myint uint64
  var mydouble float64
  var mystring string

  // Read and save an integer, double, and String to your variables.
  // scanner.Split(bufio.ScanLines)

  var tmp []string

  for scanner.Scan() {
    tmp = append(tmp, scanner.Text())
  }

  if err := scanner.Err(); err != nil {
    fmt.Fprintln(os.Stderr, "reading standard input:", err)
  }

  var err error;

  myint, err = strconv.ParseUint(tmp[0], 0, 64)
  mydouble, err = strconv.ParseFloat(tmp[1], 64)
  mystring = tmp[2]

  if( err != nil ) {
    // Something went wrong here
  }

  // Print the sum of both integer variables on a new line.
  fmt.Println(i + myint)

  // Print the sum of the double variables on a new line.
  fmt.Println(strconv.FormatFloat(d + mydouble, 'f', 1, 64))

  // Concatenate and print the String variables on a new line
  // The 's' variable above should be printed first.
  fmt.Println(s + mystring)

}
