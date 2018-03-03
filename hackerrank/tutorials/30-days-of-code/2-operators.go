package main

import (
  "fmt"
  "bufio"
  "strconv"
  "os"
)

func Round(x, unit float64) float64 {
  return float64(int64(x/unit+0.5)) * unit
}

func main() {

  // Scan the variables

  scanner := bufio.NewScanner(os.Stdin)
  var tmp []string

  for scanner.Scan() {
    tmp = append(tmp, scanner.Text())
  }

  // Convert to their types

  var mealCost float64
  var tipPercent uint64
  var taxPercent uint64

  mealCost, _ = strconv.ParseFloat(tmp[0], 64)
  tipPercent, _ = strconv.ParseUint(tmp[1], 0, 64)
  taxPercent, _ = strconv.ParseUint(tmp[2], 0, 64)

  var tip float64
  var tax float64
  var totalCost float64

  tip = mealCost * float64(tipPercent)/100
  tax = mealCost * float64(taxPercent)/100
  totalCost = Round(mealCost + tip + tax, 1)

  fmt.Println("The total meal cost is " + strconv.FormatFloat(totalCost, 'f', -1, 64) + " dollars.")
}
