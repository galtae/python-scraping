import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
move_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

res = requests.get(url)

#bs4

#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

#print(soup)

#KOSPI_now

the_tag = soup.select_one('#KOSPI_now')
print(the_tag)