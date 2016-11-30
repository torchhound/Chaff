import requests
from bs4 import BeautifulSoup as BS

def getHeadlines():
	f = open("nytHeadlines.txt", "w")
	url = "http://www.newyorktimes.com/"
	r = requests.get(url)
	rHtml = r.text
	soup = BS(rHtml, "lxml")

	for row in soup.find_all("h2", attrs = {"class" : "story-heading"}):
		f.write(row.text + "\n")

def cleanup():
	with open("nytHeadlines.txt", "r+") as f:
		for line in f:
			if not line.isspace():
				f.write(line)
