import random, string

def nameGen():
	length = random.randrange(1,1000)
	s = ""
	for i in range(length):
		s += random.choice(string.ascii_lowercase)
	print s