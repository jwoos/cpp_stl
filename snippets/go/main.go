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

type rot13Reader struct {
	r io.Reader
}

func (rotReader rot13Reader) Read(x []byte) (int, error) {
	bytesRead, err := rotReader.r.Read(x)

	for i := 0; i < bytesRead; i++ {
		if 'A' <= x[i] && x[i] <= 'Z' {
			if x[i] += 13; x[i] > 90 {
				x[i] = x[i] % 90 + 64
			}
		}

		if 'a' <= x[i] && x[i] <= 'z' {
			if x[i] += 13; x[i] > 122 {
				x[i] = x[i] % 122 + 96
			}
		}
	}

	return bytesRead, err
}

type Image struct{
	X int
	Y int
	Color uint8
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0, 0, i.X, i.Y)
}

func (i Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) At(x int, y int) color.Color {
	return color.RGBA{i.Color + uint8(x), i.Color + uint8(y), 255, 255}
}

func main() {
	fmt.Println("Hello!!")
	test()
	var anInt int = returnSomething();
	fmt.Println(anInt);
	fmt.Println(newtonsMethod(2));
}
