import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
main_content_extract = soup.find("div", id = "mw-content-text")
#get all h2 tags
headings = main_content_extract.find_all("h2")
#make a list of words to exclude
excluded_words = ["References", "External links", "See also", "or", "Notes"]
#stores cleaned headings
cleaned_headings = []
#loop through each heading tag, remove extra spaces, check if headng includes excluded words, store it if not skipping the heading
for h in headings:
    text = h.get_text().strip()
    text = text.replace("edit", "")
    skip_word = False
    for word in excluded_words:
        if word in text:
            skip_word = True
    if skip_word == False and len(text) > 0:
        cleaned_headings.append(text)
        #write results in a new text file
with open("headings.txt", "w", encoding = "utf8") as f:
    for heading in cleaned_headings:
        f.write(heading + "\n")



