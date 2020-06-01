import requests
from bs4 import BeautifulSoup
from flask import Flask

app= Flask(__name__)

@app.route('/<sign>')
def GetDocument(sign):
    url = ('https://horoskopy.cz/{}').format(sign)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content_block = soup.find("div",{"id":"content-detail"})
    todays_horoscope = soup.find("h2")
    headings = soup.find_all("div", {"class":"brown"})
    
    paragraphs = soup.find_all("p")
    result = {}
    for i in range(len(headings)):
      if i==0:
        result[headings[0].text]=paragraphs[0].text

      result[headings[i].text]=paragraphs[i].text
   
    return(result)

if __name__ == '__main__':
  app.run(host='localhost')
