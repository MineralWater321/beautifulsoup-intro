from bs4 import BeautifulSoup
import requests
from csv import writer

chapter = 1948
while chapter < 1950:
    url= "https://lnmtl.com/chapter/bringing-the-farm-to-live-in-another-world-chapter-%s"%chapter
    fileName = './chapters/BTFTLIAW - Chapter %s.txt'%chapter
    page = requests.get(url)
    textBody = []
    originalBody = []

    soup = BeautifulSoup(page.content, 'html.parser')
    header = soup.find('h3', class_="dashhead-title")

    title = header.find('span', class_="chapter-title").text
    chinese = header.find('span', class_="chapter-title")['data-content']
    headerInfo = [title, chinese]

    body = soup.find('div', class_="chapter-body")
    translated = body.find_all('sentence', class_="translated")
    original = body.find_all('sentence', class_="original")

    for content in translated:
        text = content.text.replace('\n', '')
        textBody.append(text)

    for content in original:
        characters = content.text.replace('\n', '')
        originalBody.append(characters)

    finalBody = [val for pair in zip(textBody, originalBody) for val in pair]

    with open(fileName, 'w', encoding='utf-8') as f:
        for info in headerInfo:
            f.write(info)
            f.write('\n')
            f.write('\n')
        for content in finalBody:        
            f.write(content)
            f.write('\n')
            f.write('\n')
    
    chapter += 1