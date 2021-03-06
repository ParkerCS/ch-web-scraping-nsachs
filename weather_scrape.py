
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a brief synopsis of the weather for the next 10 days.
# Include the day, date, high temp, low temp, and chance of rain.
# You can customize the text as you like, but it should be readable
# for the user.  You will need to target specific classes or other
# attributes to pull some parts of the data.
# (e.g.  Wednesday, March 22: the high temp will be 48 with a low of 35, and a 20% chance of rain). (25pts)

import urllib.request
from bs4 import BeautifulSoup

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
#soup.prettify()

#print(soup)

headers_list = [x.text.strip() for x in soup.findAll("th")]
#print(headers_list)
#rows = [x for x in soup.findAll("table").findAll("tr")]

data = [[y.text.strip() for y in x.findAll("td")] for x in soup.find("table",{"class" : "twc-table"}).findAll("tr")]

data = data[1:]
print(data)
print()

for i in range(len(data)):
    data[i] = data[i][1:]
    if i == 0:
        day = "Today"
        print(day, ", ", data[0][0][len(day):], ": the high will be ", data[0][2][:3], " with a low of", data[0][2][3:], ", and a", data[0][3], " chance of rain.")
        #Couldn't figure out how to get rid of the "ht" before the first day.
    else:
        day = data[i][0][:3]
        print("On", day, ", ", data[i][0][len(day):], ": the high will be ", data[i][2][:3], " with a low of", data[i][2][3:], ", and a", data[i][3], " chance of rain.")
    #print()



