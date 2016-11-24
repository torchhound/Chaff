import random
import requests
import json
import time
from namegenchaff import nameGen

def chaff():
	while True:
		sleepTime = random.randint(1, 30)
		print("Sleeping for {}".format(sleepTime))
		time.sleep(sleepTime)
		try:
			payload = nameGen()
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
	chaff()
	
if __name__ == "__main__":
    main()
