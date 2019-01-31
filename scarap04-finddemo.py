import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    return soup


def get_list_from_li_tag(li):

    name, price, likes, full_img_name = '', '', 0, ''

    try:
        name = li.find('dd').find('div', {'class': 'name'}).text.strip()

    except:
        print('name parsing error skip')
        pass

    try:
        price = int(li.find('dd').find('div', {'class': 'price-area'})
                    .find('strong', {'class': 'price-value'}).text.replace(',', ''))

    except:
        print('price parsing error. skip')

    try:
        likes = li.find('dd').find('div', {'class': 'other-info'}) \
                 .find('span', {'class': 'rating-total-count'}).text.strip()[1:-1]
    except:
        print('likes paring error.. skip')

    try:
        full_img_name = li.find('dt').find('img')['src']
        img_name = full_img_name.split('/')[-1]
        download_img_from_coupang('http:' + full_img_name, img_name)

    except:
        print('img_name parsing error... skip')

    return [name, price, likes, img_name]


def download_img_from_coupang(img_url, file_name):
    #print('download ...' + img_url)
    res = requests.get(img_url)

    with open('./images/' + file_name, 'wb') as f:
        f.write(res.content)


def get_product_list_from_li_tag(tag):
    product_list = []

    # print(li_list)

    for li in tag:
        product_list.append(get_list_from_li_tag(li))

    return product_list


def save_to_csv(list_of_list):
    print(list_of_list)
    df = pd.DataFrame(list_of_list, columns=['상품명', '가격', '좋아요', '이미지파일'])
    #print(type(df))
    #print(df)
    df.to_csv('./data/coupang.csv', index=False, columns=['상품명', '가격', '좋아요', '이미지파일'])


def main():

    product_list = []

    for page_num in range(1,2):
        url = 'https://www.coupang.com/np/campaigns/82/components/202952?page=' \
         + str(page_num)

        soup = get_soup_from_url(url)

        li_list = soup.find(id='productList').find_all('li')

        product_list_per_page = get_product_list_from_li_tag(li_list)

        product_list.extend(product_list_per_page)
        print(page_num, '페이지 작업완료...')

    #print(product_list_per_page)

    save_to_csv(product_list_per_page)

    #벅스 뮤직
    '''article_tag = soup\
        .find('div',{'id':'CHARTrealtime'})\
        .find('tbody').find_all('tr')[0].find('th').find('a').text
    
    print(article_tag)
    
    selector = '#CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a'
    
    title = soup.select_one(selector)
    
    #print(title)
    '''


if __name__ == "__main__":
    main()

