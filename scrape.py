#!/usr/bin/env python

import requests

from datetime import datetime
from app import db
from app.models import *

MAIN_URL = "http://search.mtvnservices.com/typeahead/suggest/?q=*%3A*+AND+schoolid_s%3A1407&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=teacherlastname_sort_s+asc&siteName=rmp&rows=20000&start=0&fl=FLAGS&prefix=schoolname_t%3A%22University+of+Alberta%22"

TAGS = {
    "first": "teacherfirstname_t",
    "last": "teacherlastname_t",
    "id": "pk_id",
    "helpfull": "averagehelpfulscore_rf",
    "clarity": "averageclarityscore_rf",
    "ease": "averageeasyscore_rf",
    "total": "total_number_of_ratings_i"
}

def addProfArgs(keys):
    """ ## build get request for our data tags"""
    tag_args = ""
    for i in keys:
        tag_args += "+" + i
    i_start = MAIN_URL.index("&fl=") + len("&fl=")
    i_fin = MAIN_URL.rindex("&prefix")
    return MAIN_URL.replace(MAIN_URL[i_start: i_fin], tag_args.strip("+"))

def generateHeader():
    """ ## Google Chrome headers
    Host: search.mtvnservices.com
    Connection: keep-alive
    Cache-Control: max-age=0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36
    Accept-Encoding: gzip, deflate, sdch
    Accept-Language: en-GB,en;q=0.8,en-US;q=0.6,am;q=0.4,hu;q=0.2,fr;q=0.2
    """
    user = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36"
    encodings = ["gzip", "deflate", "sdch", "*"]
    h = {
        "Host": "search.mtvnservices.com",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": user,
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-GB,en;q=0.8,en-US;q=0.6,am;q=0.4,hu;q=0.2,fr;q=0.2"
    }
    return h

def makeRequest(tags):
    """ ## makes http get request against target uri, returns json obj """
    u = addProfArgs(tags)

    h = generateHeader()
    r = requests.get(u) #, header=h)
    resp = r.json()
    return resp


def updateProfs():
    """ ## Update our db with any new data if we need to
    - We do this by checking the numFound variable in the response since that'll at least tell us if theres been a new prof added, which guarenties a db update on our end
    - Also we get all our db entries at once to try and save time (could create db meta table for keeping track of length and such, keep our db calls small / fast)
    """

    #if datetime.utcnow.isoformat()

    u = addProfArgs([TAGS["first"], TAGS["last"], TAGS["id"]])
    r = requests.get(u)

    # get our data fromt he site as well as the db
    resp = r.json()
    profs = Professor.query.all()


    # do nothing if we still have the same lengths, means we'rer probs still up to date otherwise
    # the names and ids wont ever change so no need to go updating our db, just add in the new values
    if profs and resp["response"]["numFound"] != len(profs):
        # boss 1-liner, cause i can
        """
        [ db.session.add(Professor(e[TAGS["id"]], last=e[TAGS["last"]], first=e[TAGS["first"]])) for e in r.json()["response"]["docs"] if e[TAGS["id"]] not in [i.id for i in profs] ]
        """

        for e in r.json()["response"]["docs"]:
            if e[TAGS["id"]] not in [i.id for i in profs]:
                print e
                p = Professor(e[TAGS["id"]], last=e[TAGS["last"]], first=e[TAGS["first"]])
                db.session.add(p)

    else:
        for e in r.json()["response"]["docs"]:
            print e
            p = Professor(e[TAGS["id"]], last=e[TAGS["last"]], first=e[TAGS["first"]])
            db.session.add(p)

    db.session.commit()
    # get the actul prof data from the mtv site
    u = addProfArgs([TAGS["id"], TAGS["ease"], TAGS["helpfull"], TAGS["total"], TAGS["clarity"] ])
    r = requests.get(u)
    resp = r.json()

def main():
    updateProfs()

if __name__ == '__main__':
    main()
