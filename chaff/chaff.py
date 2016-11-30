import random
from multiprocessing import Process
import requests
import json
import time
from nytHeadlines import getHeadlines, cleanup

def updateHeadlines():
	time.sleep(1800)
	getHeadlines()
	cleanup()
	updateHeadlines()

def parseHeadlines():
	try:
		f = open("nytHeadlines.txt").readlines()
		line = f[random.randrange(0, len(f))]
		words = line.split()
		result = random.choice(words)
		return result
	except Exception as e:
		print(e)
		parseHeadlines()

def chaff():
	while True:
		sleepTime = random.randint(1, 30)
		print("Sleeping for {}".format(sleepTime))
		time.sleep(sleepTime)
		try:
			payload = parseHeadlines()
			print("Searching for {}".format(payload))
			response = requests.get("http://api.duckduckgo.com/?q=" + payload + "&format=json&pretty=1")
			#jsonOut = json.loads(response.content)
			print("Status: {}".format(response.status_code))
			#for x in jsonOut['RelatedTopics']:
				#print(RelatedTopics['Result']
			#for x in jsonOut['Results']:
				#print(Results['Result']
			#print("Results: {}".format(jsonOut["RelatedTopics"]["Result"]))
			#print("Results: {}".format(jsonOut["Results"]["Result"]))
			print(response.json())
		except Exception as e:
			print(e)
			pass

def main():
	cleanup()
	p1 = Process(target=chaff())
	p2 = Process(target=updateHeadlines())
	p1.daemon = True
	p2.daemon = True
	p1.start()
	p2.start()
	
if __name__ == "__main__":
    main()
