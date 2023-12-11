package utils

func Contains[K comparable](arr []K, x K) bool {
	for _, v := range arr {
		if x == v {
			return true
		}
	}
	return false
}

func ContainsString(arr []string, x string) bool {
	for _, v := range arr {
		if x == v {
			return true
		}
	}
	return false
}
