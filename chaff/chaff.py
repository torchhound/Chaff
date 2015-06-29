import anonbrowser, namegenerator, mechanize, random
from namegenchaff import nameGen

def chaff():
	time = random.randrange(1,60)
	payload = namegenchaff.nameGen()
	anonbrowser.anonbrowser()
	#send payload as search request
	#for x in time:
	while (time != 0):
		time --	

def main():
	#give user start and stop options
	#implement key words instead of just randomly generated junk
	z = True
	while (z == True):
		chaff()
	
if __name__ == "__main__":
    main()