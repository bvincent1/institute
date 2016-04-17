import requests
from app import db
from app.models import Professor

global MAIN_URL
global TAGS

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
    global MAIN_URL
    if len(keys) > 4:
        raise Exception
    else:
        tag_args = ""
        for i in keys:
            tag_args += "+" + i
        MAIN_URL = MAIN_URL.replace("FLAGS", tag_args.strip("+"))

def updateProfs():
    addProfArgs([TAGS["first"], TAGS["last"], TAGS["id"]])
    r = requests.get(MAIN_URL)

    for i in r.json()["response"]["docs"]:
        print i
        p = Professor(i[TAGS["id"]], last=i[TAGS["last"]], first=[TAGS["first"]])
        db.session.add(p)
    db.session.commit()



def main():
    updateProfs()

if __name__ == '__main__':
    main()
