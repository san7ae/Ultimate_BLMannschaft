import requests, bs4
import csv

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

page = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/saison_id/2000/plus/0/galerie/0/page/"
pageTree = requests.get(page, headers=headers)
pageSoup = bs4.BeautifulSoup(pageTree.content, 'html.parser')

outfile = open('main.csv','w', encoding="utf-8", newline='')
writer = csv.writer(outfile, delimiter=" ")
writer.writerow(["Players", "Values", "Position", "Nationality"])

paging = pageSoup.find("div",{"class":"pager"}).find("ul",{"class":"yiiPager"}).find_all("a")
start_page = paging[0].text
last_page = paging[len(paging)-3].text


totalPlayer = 0
pages = list(range(1,int(last_page)+1))
for page in pages:
    url = 'https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/saison_id/2000/plus/0/galerie/0/page/'+ str(page)
    html = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(html.content, 'html.parser')

    #Print the page
    print("======================================================================================")
    print ('Processing page: %s' %(page))
    print("======================================================================================")


    product_name_list = soup.findAll("tr", {"class":{"even","odd"}})
    for element in product_name_list:
        player = element.find("a",{"class":"spielprofil_tooltip"}).text
        value = element.find("td", {"class": "rechts hauptlink"}).text.replace(u"\u00a3", "").replace("m","").replace(".",",")
        position = element.select("td")[4].text

        nationality = []
        nationality1 = element.select("td[class*='zentriert'] img[class*='flaggenrahmen']")[0].attrs["title"]
        nationality.append(nationality1)



        print(player)
        writer.writerow([player, value, position, nationality])
        totalPlayer+=1


outfile.close()
print("======================================================================================")
print("TOTAL OF PLAYERS: " + str(totalPlayer))
print ('Done')