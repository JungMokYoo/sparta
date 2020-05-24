import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')


movies = soup.select('.newest-list > div > table > tbody > tr')



for tag in soup.find_all("span", {'class':'rank'}):
    tag.replaceWith('')



for movie in movies:
    list_tag = movie.select_one('td')
    if list_tag is not None:
        num = list_tag = movie.select_one('td.number').text.strip()
        song_title = movie.select_one('td:nth-child(5) > a').text.strip()
        singer = movie.select_one('td:nth-child(5) > a:nth-child(2)').text
    print(num,song_title,singer)
        
    