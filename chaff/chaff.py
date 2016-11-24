import random
import requests
import json
from namegenchaff import nameGen

def chaff():
	while True:
		try:
			payload = nameGen()
			print("Searching for {}".format(payload))
			response = requests.get("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + payload)
			#if response.status_code == 
			#jsonOut = json.loads(response.text)
			#print("Status: {}".format(jsonOut["responseStatus"]))
			#print("Results: {}".format(jsonOut["responseData"]["results"]))
			print(response.json())
		except Exception as e:
			print(e)
			pass

def main():
	chaff()
	
if __name__ == "__main__":
    main()
