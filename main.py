import requests, bs4
import csv

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

page = "https://www.transfermarkt.de/1-bundesliga/torschuetzenliste/wettbewerb/L1/ajax/yw1/saison_id/2018/altersklasse/alle/detailpos//plus/2/page/"
pageTree = requests.get(page, headers=headers)
pageSoup = bs4.BeautifulSoup(pageTree.content, 'html.parser')

# Write to CSV data
outfile = open('main.csv','w', encoding="utf-8", newline='')
writer = csv.writer(outfile, delimiter=",")
writer.writerow(["Name", "Verein", "Position", "Einsatz", "Alter", "Vorlagen", "Elfmetertor", "Tore"])


# Define Pagination
paging = pageSoup.find("div",{"class":"pager"}).find("ul",{"class":"yiiPager"}).find_all("a")
start_page = paging[0].text
last_page = paging[len(paging)-3].text

#Start to scrape

totalPlayer = 0
pages = list(range(1,int(last_page)+1))
for page in pages:
    url = 'https://www.transfermarkt.de/1-bundesliga/torschuetzenliste/wettbewerb/L1/ajax/yw1/saison_id/2018/altersklasse/alle/detailpos//plus/2/page/'+ str(page)
    html = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(html.content, 'html.parser')

    #Print the page
    print("======================================================================================")
    print ('Processing page: %s' %(page))
    print("======================================================================================")


    player_list = soup.findAll("tr", {"class":{"even","odd"}})
    for element in player_list:
        try:
            name = element.find("a",{"class":"spielprofil_tooltip"}).text
            position = element.find("table").findAll("td")[2].text
            alterStr = element.findAll("td")[6].text[:2]
            alter = int(alterStr)

            try:
                verein = element.findAll("td")[7].find("img").attrs["alt"]
            except:
                verein = 'Spiel für mehrere Vereine'

            einsatzStr = element.findAll("td")[8].text
            einsatz = float(einsatzStr)

            vorlage = element.findAll("td")[9].text

            elfmeterStr = element.findAll("td")[10].text
            elfmeter = float(elfmeterStr)

            # spielminuten = element.findAll("td")[11].text

            toreStr = element.findAll("td")[14].text
            tore = float(toreStr)
            # minutenProTor = element.findAll("td")[12].text
            # toreProSpiel = element.findAll("td")[13].text

            #value = element.find("td", {"class": "rechts hauptlink"}).text.replace(u"\u00a3", "").replace("m","").replace(".",",")

            #nationality = []
            #nationality1 = element.select("td[class*='zentriert'] img[class*='flaggenrahmen']")[0].attrs["title"]
            #nationality.append(nationality1)

            print(name)
            writer.writerow([name, verein, position, einsatz, alter, vorlage, elfmeter, tore])
            totalPlayer+=1

        except:
            print("An exception occurred")

outfile.close()
print("======================================================================================")
print("TOTAL OF PLAYERS: " + str(totalPlayer))
print ('Done')