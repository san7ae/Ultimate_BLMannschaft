import requests, bs4
import csv

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

page = "https://www.transfermarkt.de/1-bundesliga/marktwertaenderungen/wettbewerb/L1/page/"
pageTree = requests.get(page, headers=headers)
pageSoup = bs4.BeautifulSoup(pageTree.content, 'html.parser')

# Write to CSV data
outfile = open('transfermarktValue.csv','w', encoding="utf-8", newline='')
writer = csv.writer(outfile, delimiter=",")
writer.writerow(["Name", "Value"])


# Define Pagination
paging = pageSoup.find("div",{"class":"pager"}).find("ul",{"class":"yiiPager"}).find_all("a")
start_page = paging[0].text
last_page = paging[len(paging)-3].text

#Start to scrape

totalPlayer = 0
pages = list(range(1,int(last_page)+1))
for page in pages:
    url = 'https://www.transfermarkt.de/1-bundesliga/marktwertaenderungen/wettbewerb/L1/page/'+ str(page)
    html = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(html.content, 'html.parser')

    #Print the page
    print("======================================================================================")
    print ('Processing page: %s' %(page))
    print("======================================================================================")


    player_list = soup.findAll("tr", {"class":{"even","odd"}})
    for element in player_list:
        name = element.find("a", {"class": "spielprofil_tooltip"}).text
        wert = element.find("td", {"class": {"rechts hauptlink mwHoechstwertKarriere", "rechts hauptlink"}})
        valueStr = wert.text.replace(",", ".").replace(" Mio. €","").strip()
        value = float(valueStr)

        # nationality = []
        # nationality1 = element.select("td[class*='zentriert'] img[class*='flaggenrahmen']")[0].attrs["title"]
        # nationality.append(nationality1)

        print(name)
        writer.writerow([name, value])
        totalPlayer += 1

outfile.close()
print("======================================================================================")
print("TOTAL OF PLAYERS: " + str(totalPlayer))
print ('Done')