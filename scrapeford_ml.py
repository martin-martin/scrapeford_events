# -*- coding: utf-8 -*-
# notifications about interesting events
# for my friend who's hanging out where I used to
import re
import requests
import webbrowser
import time
from bs4 import BeautifulSoup


# ------------- SETUP - CHANGE THINGS HERE ------------- #

# regex pattern to find all things AI and ML etc.
pattern = re.compile(r"[Mm]achine|ML|AI|[Ii]ntelligence|[Rr]obot|[Mm]aker")
# define how long the user should have to look at the results
# before the searchable map opens
wait_time = 5
# scraping from the Stanford daily events page
page_url = "https://events.stanford.edu/today"
# stub for linking to the event description pages
page_stub = "https://events.stanford.edu"
page = requests.get(page_url)
soup = BeautifulSoup(page.text, "html.parser")
# events are contained within "postcard-link" classed <a>s
all_events = soup.findAll("a", {"class": "postcard-link"}, href=True)


# ------------- ONE FUNCTION ------------- #

def get_events(all_events):
    flag = False
    cool_stuff = list()

    for event in all_events:
        if re.search(pattern, event.get_text()):
            flag = True
            link = page_stub + event['href']
            text = event.get_text()
            cool_stuff.append((link, text))
    if flag:
        print("\n###################################################")
        print("YJay! Check out these interesting on-campus events:")
        print("###################################################\n")
        for event in cool_stuff:
            # opening the event's detail page
            webbrowser.open(event[0])
            # and displaying the info in the console
            print(event[1])
        # giving a bit of time to take in the results!
        time.sleep(wait_time)
        # opening the searchable map in order to find out
        # how to get there quickly
        webbrowser.open("https://campus-map.stanford.edu/")
    # save the resulting list of tuples, just for fun
    return cool_stuff


# ------------- RUN THAT STUFF ------------- #

event_list = get_events(all_events)
# print some feedback if there are no matching events
if not event_list:
    print("Take today off. There's nothing going on that interests you.")
