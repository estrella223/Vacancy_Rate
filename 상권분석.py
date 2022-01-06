import pandas as pd
import matplotlib.pyplot as plt

'''파일 불러오기'''
seouldf = pd.read_csv('서울시우리마을가게상권분석서비스(상권-추정매출)_2020.csv',encoding = '949')
seouldf = pd.DataFrame(seouldf)
# print(seouldf)
'''필요한 열만 쓰도록 자르기'''
need_name = seouldf.iloc[:,[0,1,7,8]]
need_name = need_name.set_index(['기준_년_코드'],drop= True)
# need_name.index.name="업종"
need_name= need_name.sort_values(by = '기준_분기_코드',ascending=True)
# print(need_name)

'''특정 업종만 보기(마스크 씌우기) - 음식서비스'''
#
foodserv = need_name.query('서비스_업종_코드_명.str.contains("한식음식점|일식음식점|양식음식점|중식음식점|분식음식점|반찬가게|패스트푸드|치킨전문점|제과점")', engine='python')
foodstore = need_name.query('서비스_업종_코드_명.str.contains("슈퍼마켓|편의점")', engine = 'python')
farm = need_name.query('서비스_업종_코드_명.str.cont`ains("청과상|육류판매|수산물판매")', engine = 'python')
sports = need_name.query('서비스_업종_코드_명.str.contains("스포츠강습|스포츠클럽|운동/경기용품|골프연습장")', engine = 'python')
# 노가다
# foodserv_1=(need_name['기준_분기_코드'] == 1)
# sell_total = need_name[foodserv_1]
# sell_total1 = sell_total['분기당_매출_금액'].sum()
# # print(foodserv_kor)
# print(sell_total1)

#실패한 반복문
# for i in foodserv:
#     i=0
#     if i <= 4:
#         i += 1
#         foodserv_1 = need_name['기준_분기_코드'] == i
#         sell_total = need_name[foodserv_1]
#         sell_total1 = sell_total['분기당_매출_금액'].sum()
#         print(int(sell_total1))
def findcell(filter):
    i=0
    sellall = []
    while i < 5 :
        i += 1
        findqua = filter['기준_분기_코드'] == i
        sell_total = filter[findqua]
        sell_total1 = sell_total['분기당_매출_금액'].sum()
        sellall.append(sell_total1)
        if i == 4:
            break
    return sell_total1
    print(sellall)

data = {'상품명': ['2020 1/4', '2020 2/4', '2020 3/4', '2020 4/4'],
        '음식서비스': findcell(foodserv),
        '농축수산물': findcell(farm),
        '음식료품': findcell(foodstore),
        '스포츠,레저': findcell(sports)}
df = pd.DataFrame(data)
print(df)
# df2 = df.set_index("상품명", drop=True)
