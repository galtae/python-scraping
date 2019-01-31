import requests
from bs4 import BeautifulSoup

move_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
best_url = 'http://www.yes24.com/24/category/bestseller'
sin_url = 'http://www.yes24.com/24/Category/NewProduct'

res = requests.get(sin_url)

soup = BeautifulSoup(res.text, 'html.parser')

selector = '#old_content > table > tbody > tr:nth-child(2) > td.title > div > a'
selector_1 = '#bestList > ol > li.num1 > p:nth-child(3) > a'
selector_2 = '#topBooksUl_001 > li:nth-child(1) > div.goods_info > p.goods_name > a'

#the_tag = soup.select_one(selector)
#the_tag1 = soup.select_one(selector_1)
the_tag2 = soup.select_one(selector_2)

#print (the_tag.text)
#print (the_tag1.text)
print(the_tag2.text)
