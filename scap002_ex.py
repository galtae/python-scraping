import requests
from bs4 import BeautifulSoup


url = 'https://www.coupang.com/np/campaigns/82/components/202952'

res = requests.get(url)

selector = '#\\32 575627 > a > dl > dd > div.name'
selector_1 = '#\\32 575627 > a > dl > dd > div.price-area > div:nth-child(1) > div.price > em > strong'

soup = BeautifulSoup(res.text, 'html.parser')

#the_tag = soup.select_one(selector)
#the_tag1 = soup.select_one(selector_1)

product_title = soup.select_one(selector).text
product_price = soup.select_one(selector_1).text

print (product_title.strip())
print (product_price)
