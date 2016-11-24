import random
import string

def nameGen():
	s = ""
	for i in range(1, random.randrange(1, 100)):
		if i == random.randrange(1, 100): #need a better way to add spaces
			s += " "
		s += random.choice(string.ascii_lowercase)
	#print(s)
	return s

def main():
	nameGen()

if __name__ == "__main__":
	main()
