from scrapely import Scraper

s = Scraper()

url = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=279686"
data = {'Overall Quality': '5.0', "Helpfulness": "4.9", "Clarity": "5.0", "Easiness": "3.3"}

s.train(url, data)


r = s.scrape("http://www.ratemyprofessors.com/ShowRatings.jsp?tid=414256")
print(r)
