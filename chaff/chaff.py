import random
import requests
from threading import Thread
import json
import time
from nytHeadlines import getHeadlines, cleanup

def updateHeadlines():
	print("Starting 30 minute countdown to next headline refresh")
	time.sleep(1800)
	getHeadlines()
	cleanup()
	updateHeadlines()

def parseHeadlines(): #parse out common words and/or search for more than one word
	try:
		f = open("nytHeadlines.txt").readlines()
		line = f[random.randrange(0, len(f))]
		words = line.split()
		result = random.choice(words)
		if result == "Cannot choose from an empty sequence":
			parseHeadlines()
		else:
			return result
	except Exception as e:
		#print(e)
		parseHeadlines()

def chaff():
	while True:
		sleepTime = random.randint(1, 30)
		print("Sleeping for {}".format(sleepTime))
		time.sleep(sleepTime)
		try:
			payload = parseHeadlines()
			if payload == None:
				payload = parseHeadlines()
			print("Searching for {}".format(payload))
			response = requests.get("http://api.duckduckgo.com/?q=" + payload + "&format=json&pretty=1")
			print("Status: {}".format(response.status_code))
			print(response.json())
		except Exception as e:
			print(e)
			pass

def main():
	cleanup()
	Thread(target = chaff).start()
	Thread(target = updateHeadlines).start()

if __name__ == "__main__":
    main()
