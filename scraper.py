from bs4 import BeautifulSoup
import requests

for i in range(1, 20):

    r = requests.get('http://www.subdivx.com/index.php?buscar=silicon+valley+s02e0'+str(i)+'&accion=5&masdesc=&subtitulos=1&realiza_b=1').text
    soup = BeautifulSoup(r, "lxml")

    sr = requests.get(soup.find_all('a', class_="titulo_menu_izq")[0].get('href')).text
    ssoup = BeautifulSoup(sr, "lxml")

    file = open('scraped_stuff/Silicon.Valley.S01.E0' + str(i) + ".srt", 'w')
    file.write(requests.get(ssoup.find_all('a', class_="link1")[0].get('href')).text)
    file.close()
