import requests    # 웹크롤링 위해 필요
from bs4 import BeautifulSoup    # 웹크롤링 위해 필요
import pandas as pd    # 크롤링 결과 df로 저장할 때 필요

# https://arehoow.tistory.com/9    크롤링
# https://mizykk.tistory.com/71    txt저장

start = 1    # 페이지 초기값
result_df = pd.DataFrame()    # 데이터프레임으로 만들기 위해
while start < 600:    # 600개만 뽑기위해
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%BD%94%EB%A1%9C%EB%82%98&sort=0&photo=0&field=0&pd=3&ds=2020.11.01&de=2021.02.28&cluster_rank=38&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:from20201101to20210228,a:all&start={}'.format(start)    # url주소
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    news_title = [title['title'] for title in soup.find_all('a', attrs={'class': 'news_tit'})]  # 기사 제목 찾기

    df = pd.DataFrame({'기사제목': news_title})    # 데이터 프레임
    result_df = pd.concat([result_df, df], ignore_index=True)    # 합쳐서 저장
    start += 10    # 다음페이지로 넘기기 위해 10씩 증가시킴
    # print(result_df)
    result_df.to_csv('테스트.txt', sep = '\t', index=False, header=True)    # txt파일로 저장