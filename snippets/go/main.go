package main

import (
	"fmt"
	"math"
)

func test() {
	for i := 0; i < 10; i++ {
		fmt.Println(i);
	}
}

func returnSomething() int {
	return 1;
}

func newtonsMethod(x float64) float64 {
	var current float64 = 1
	var prev float64 = 2
	var delta float64 = 0.00001

	for delta <= math.Abs(current - prev)  {
		temp := current - ((math.Pow(current, 2) - x) / (2 * current))
		prev = current
		current = temp
	}

	return current
}

func main() {
	fmt.Println("Hello!!")
	test()
	var anInt int = returnSomething();
	fmt.Println(anInt);
	fmt.Println(newtonsMethod(2));
}
