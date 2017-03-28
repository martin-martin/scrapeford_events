# -*- coding: utf-8 -*-
# notifications about interesting events for my friend hanging out where I used to
import re
import requests
import webbrowser
import time
from bs4 import BeautifulSoup
from pprint import pprint

# regex pattern to find all things AI and ML etc.
#pattern = re.compile(r"[Mm]achine|ML|AI|[Ii]ntelligence|[Rr]obot|[Mm]aker")
# testing with today available events
pattern = re.compile(r"[Gg]raduate")
# define how long the user should have to look at the results before the searchable map opens
wait_time = 5

# scraping from the Stanford daily events page
page_url = "https://events.stanford.edu/today/"
page = requests.get(page_url)
soup = BeautifulSoup(page.text, "html.parser")

# events are contained withtin "postcard-text" classed divs
all_events = soup.findAll("div", {"class" : "postcard-text"})
flag = False
cool_stuff = list()

for event in all_events:
	if re.search(pattern, event.get_text()):
		flag = True
		cool_stuff.append(event.get_text())
if flag:
	print("##########################################################################")
	print("YJay! There's something interesting happening for you today! Check it out:")
	print("##########################################################################")
	for event in cool_stuff:
		print(event)
	# giving a bit of time to take in the results!
	time.sleep(wait_time)
	# opening the searchable map in order to find out how to get there quickly
	webbrowser.open("https://campus-map.stanford.edu/")