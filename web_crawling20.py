import requests    # 웹크롤링 위해 필요
from bs4 import BeautifulSoup    # 웹크롤링 위해 필요
import pandas as pd    # 크롤링 결과 df로 저장할 때 필요

# https://arehoow.tistory.com/9    크롤링
# https://mizykk.tistory.com/71    txt저장

start = 1
result_df = pd.DataFrame()
while start < 600:
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B3%B5%EC%8B%A4%EB%A5%A0&sort=0&photo=0&field=0&pd=3&ds=2020.01.01&de=2020.03.31&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20200101to20200331,a:all&start={}'.format(
            start)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    news_title = [title['title'] for title in soup.find_all('a', attrs={'class': 'news_tit'})]  # 기사 제목

    df = pd.DataFrame({'기사제목': news_title})
    result_df = pd.concat([result_df, df], ignore_index=True)
    start += 10
    # print(result_df)
    result_df.to_csv('web_crawling20_1분기.txt', sep = '\t', index=False, header=True)