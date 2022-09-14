from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://lnmtl.com/chapter/bringing-the-farm-to-live-in-another-world-chapter-1943"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('h3', class_="dashhead-title")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n', '')

        info = [title, location, price, area]
        thewriter.writerow(info)
        