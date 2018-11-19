package main

import (
	"bufio"
	"fmt"
	"os"
)

func prompt(ask string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(ask)
	text, _ := reader.ReadString('\n')
	return text
}
