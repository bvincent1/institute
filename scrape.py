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
    """ ## Add correct key-values to GET request, modifies the """
    global MAIN_URL
    if len(keys) > 4:
        raise Exception
    else:
        tag_args = ""
        for i in keys:
            tag_args += "+" + i
        i_start = MAIN_URL.index("&fl=") + len("&fl=")
        i_fin = MAIN_URL.rindex("&prefix")
        MAIN_URL = MAIN_URL.replace(MAIN_URL[i_start: i_fin], tag_args.strip("+"))

def updateProfs():
    """ ## Update our db with any new data if we need to
    - We do this by checking the numFound variable in the response since that'll at least tell us if theres been a new prof added, which guarenties a db update on our end
    - Also we get all our db entries at once to try and save time (could create db meta table for keeping track of length and such, keep our db calls small / fast)
    """
    addProfArgs([TAGS["first"], TAGS["last"], TAGS["id"]])
    r = requests.get(MAIN_URL)

    # get our data fromt he site as well as the db
    resp = r.json()
    profs = Professor.query.all()

    # do nothing if we still have the same lengths, means we'rer probs still up to date otherwise
    # the names and ids wont ever change so no need to go updating our db, just add in the new values
    if resp["response"]["numFound"] != len(profs):
        # boss 1-liner, cause i can
        """
        [ db.session.add(Professor(e[TAGS["id"]], last=e[TAGS["last"]], first=e[TAGS["first"]])) for e in r.json()["response"]["docs"] if e[TAGS["id"]] not in [i.id for i in profs] ]
        """

        for e in r.json()["response"]["docs"]:
            if e[TAGS["id"]] not in [i.id for i in profs]:
                print e
                p = Professor(e[TAGS["id"]], last=e[TAGS["last"]], first=e[TAGS["first"]])
                db.session.add(p)
        db.session.commit()



def main():
    updateProfs()

if __name__ == '__main__':
    main()
