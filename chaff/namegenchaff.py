import random
import string

def nameGen():
	s = ""
	for i in range(1, random.randrange(1,150)):
		s += random.choice(string.ascii_lowercase)
	print(s)
	return s

def main():
	nameGen()

if __name__ == "__main__":
	main()
