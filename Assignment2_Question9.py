import csv

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
main_content_extract = soup.find("div", id = "mw-content-text")
tables = main_content_extract.find_all("table")
target_table = None
#loop through tables and get rows in tables
for table in tables:
    rows = table.find_all("tr")
    #list collects rows that contain data rows.
    data_rows = []
    for r in rows:
        if r.find_all("td"):
            data_rows.append(r)
            #if table has 3 or more data rows, keep it and stop looking for more
    if len(data_rows) >= 3:
        target_table = table
        break
        #continue if there is a valid target table
if target_table:
    #get all rows for the table
    rows = target_table.find_all("tr")
    first_row = rows[0]
    #check if it contains th cells
    header_cells = first_row.find_all("th")
    #if there are header rows, us them as the column names
    if len(header_cells) > 0:
        headers = []
        for h in header_cells:
            headers.append(h.get_text())
        data_rows = rows
        #if there's no header still write the table, but the headers will be empty.
    else:
        first_cells = first_row.find_all("td")
        headers = []
        data_rows = rows
        #create and write to a csv file
    with open("wiki_table.csv", "w", newline = "", encoding="utf-8") as f:
        writer = csv.writer(f)
        #write header row
        writer.writerow(headers)
        #write each table row
        for row in data_rows:
            cells = row.find_all(["td","th"])
            row_data = []
            for cell in cells:
                row_data.append(cell.get_text())
            writer.writerow(row_data)
