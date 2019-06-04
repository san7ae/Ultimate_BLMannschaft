import requests, bs4
import csv

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.ligainsider.de/bundesliga/ranking-top-10/geblockte-baelle/"
pageTree = requests.get(page, headers=headers)
pageSoup = bs4.BeautifulSoup(pageTree.content, 'html.parser')

# Write to CSV data
outfile = open('geblockte-baelle.csv','w', encoding="utf-8", newline='')
writer = csv.writer(outfile, delimiter=" ")
writer.writerow(["Name", "Verein", "Position", "Einsatz", "SpielMinuten", "balleroberungen"])


player_list = pageSoup.findAll("tr")

for element in player_list:
    try:
        name = element.find("a").text
        verein = element.find("a", {"class":"text-thin"}).text
        position = element.findAll("td", {"class": "text-left"})[2].text

        einsatzStr = element.findAll("td", {"class": "text-right"})[0].text
        einsatz = int(einsatzStr)

        spielminutenStr = element.findAll("td", {"class":"text-right"})[1].text
        spielminuten = int(spielminutenStr)

        geblockteBaelleStr = element.findAll("td", {"class": "text-right"})[2].text
        geblockteBaelle = int(geblockteBaelleStr)




        print(name)
        writer.writerow([name, verein, position, einsatz, spielminuten, geblockteBaelle])
    except:
        print("An exception occurred")






outfile.close()
print("======================================================================================")
print ('Done')