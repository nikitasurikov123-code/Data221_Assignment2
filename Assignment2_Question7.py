import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
#the url wasn't working, so I had to use this
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#find title tag and extract it
title = soup.find("title").get_text()
print("Page title: " + title)
main_content_of_page = soup.find("div", id = "mw-content-text")
#get paragraph contents
paragraphs = main_content_of_page.find_all("p")
#loop through paragraphs and print the one that is long enough
for p in paragraphs:
    text = p.get_text().strip()
    if len(text) >= 50:
        print("\nFirst Paragraph:")
        print(text)
        break

#https://stackoverflow.com/questions/51154114/python-request-get-fails-to-get-an-answer-for-a-url-i-can-open-on-my-browser
#headers help