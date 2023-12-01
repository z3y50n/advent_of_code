package utils

import (
	"log"
	"os"
	"strings"
)

func ReadS(filename string) []string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	s := string(data)
	lines := strings.Split(s, "\n")

	return lines

}
