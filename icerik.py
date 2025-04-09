import requests
from bs4 import BeautifulSoup

def content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    baslik = soup.find("h1")
    title = baslik.get_text().strip() if baslik else ""

    zaman = soup.find("time")
    date = zaman.get_text().strip() if zaman else ""

    paragraf = soup.find_all("p")
    content = ""
    for p in paragraf:
        content += p.get_text().strip() + "\n"

    data = 'Tarih: {}\nBaşlık: {}\nİçerik:\n{}\n'.format(date, title, content)

    with open("haber_kayitlari.txt", "a", encoding="utf-8") as file:    
        file.write(data + "\n")

content("https://www.milligazete.com.tr/haber/24244937/serdar-haydanli-kimdir")
