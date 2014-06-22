import random
import string
def namegen():
	length = random.randrange(1,1000)
	s = ""
	for i in range(length):
		s += random.choice(string.ascii_lowercase)
	print s
main()