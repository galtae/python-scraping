import requests
from bs4 import BeautifulSoup

url ='https://www.coupang.com/np/campaigns/82/components/202952'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

product_list = soup.select('#productList > li')


for li in product_list :
    print(li)
    print('================================')


#print(product_list)