/*
This application uses channels to create a pipeline of goroutines.
The pipeline consists of two goroutines: a generator and a transformer.
The main function uses the generator and transformer goroutines.
*/

package main

/*
Add imports for formatting, random number generation, and time.
*/

import (
	"fmt"
	"math/rand"
	"time"
)

/*
Create a goroutine 'generator' 
Arguments:
- 'numbers': target channel of the generator.
- 'min': minimum unsigned value of the generated numbers.
- 'max': maximum unsigned value of the generated numbers.
Details:
- Generates integer values between `min` and `max` and sends them to the `numbers` channel.
- It closes the channel when it is done.
- Produces numbers at an irregular pace by adding a random delay between 50 and 200 milliseconds.
*/

func generator(numbers chan<- int, min, max uint64) {
	defer close(numbers)
	for {
		num := rand.Intn(int(max-min)) + int(min)
		numbers <- num
		time.Sleep(time.Duration(rand.Intn(150)+50) * time.Millisecond)
	}
}

/*
Create a goroutine 'transformer'
Arguments:
- 'numbers': source channel of the transformer.
- 'cubes': target channel of the transformer.
Details:
- Receives numbers from the `numbers` channel.
- Calculates the cube of each number
- Sends the result to the `cubes` channel.
- It continues this process until the `numbers` channel is closed, and then it closes the `cubes` channel.
*/
func transformer(numbers <-chan int, cubes chan<- int) {
	defer close(cubes)
	for num := range numbers {
		cubes <- num * num * num
	}
}
/*
Create a 'main' function as the entry point of the program.
Details:
- It creates two channels, `numbers` and `cubes`, and starts two goroutines: `generator` and `transformer`.
- It then receives values from the `cubes` channel and prints them.
*/
func main() {
	numbers := make(chan int)
	cubes := make(chan int)

	go generator(numbers, 0, 100)
	go transformer(numbers, cubes)

	for cube := range cubes {
		fmt.Println(cube)
	}
}


