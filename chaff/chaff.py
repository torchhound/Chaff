import mechanize #mechanize incompatible with python3
import random
import json
from namegenchaff import nameGen
from anonbrowser import anonbrowser

def chaff():
	payload = nameGen()
	ab = anonBrowser(proxies = [])
	while True:
		try:
			ab.anonymize()
			print("Searching for {}".format(payload))
			response = ab.open("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + payload)
			jsonOut = json.loads(response)
			print("Status: {}".format(jsonOut["responseStatus"]))
			print("Results: {}".format(jsonOut["responseData"]["results"]))
		except Exception as e:
			print(e)
			pass

def main():
	chaff()
	
if __name__ == "__main__":
    main()
