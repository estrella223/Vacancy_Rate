import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

stores19 = pd.read_csv('서울시 우리마을가게 상권분석서비스(상권-추정매출)_2019.csv', encoding='cp949')
stores19.rename(columns={'기준_년_코드':'연도', '기준_분기_코드': '분기', '서비스_업종_코드_명': '상품명',
                         '분기당_매출_금액': '매출액'}, inplace=True)

stores19 = stores19.set_index("연도")

stores19 = stores19[["분기", "상품명", "매출액"]]
# print(stores19)

# https://zephyrus1111.tistory.com/46
# 음식료품
market_total = stores19.query('상품명.str.contains("슈퍼마켓|편의점")', engine='python')    # 음식서비스 추출
# print(market_total)

mask_market_total1 = market_total["분기"] == 1    # 음식료품 1분기 마스크
market_total1 = market_total[mask_market_total1]    # 음식료품 1분기만
market_total1_sum = market_total1['매출액'].sum()    #음식료품 1분기 매출액 합
# print(market_total1)
# print(market_total1_sum)
mask_market_total2 = market_total["분기"] == 2    # 음식료품 2분기 마스크
market_total2 = market_total[mask_market_total2]    # 음식료품 2분기만
market_total2_sum = market_total2['매출액'].sum()    #음식료품 2분기 매출액 합
# print(market_total2)
# print(market_total2_sum)
mask_market_total3 = market_total["분기"] == 3    # 음식료품 3분기 마스크
market_total3 = market_total[mask_market_total3]    # 음식료품 3분기만
market_total3_sum = market_total3['매출액'].sum()    #음식료품 3분기 매출액 합
# print(market_total3)
# print(market_total3_sum)
mask_market_total4 = market_total["분기"] == 4    # 음식료품 4분기 마스크
market_total4 = market_total[mask_market_total4]    # 음식료품 4분기만
market_total4_sum = market_total4['매출액'].sum()    #음식료품 4분기 매출액 합
# print(market_total4)
# print(market_total4_sum)


# 음식서비스
service_total = stores19.query('상품명.str.contains("반찬가게|분식전문점|양식음식점|일식음식점|제과점|중식음식점|치킨전문점|커피-음료|패스트푸드점|한식음식점")', engine='python')    # 음식서비스 추출
# print(service_total)

mask_service_total1 = service_total["분기"] == 1    # 음식서비스 1분기 마스크
service_total1 = service_total[mask_service_total1]    # 음식서비스 1분기만
service_total1_sum = service_total1['매출액'].sum()    #음식서비스 1분기 매출액 합
# print(service_total1)
# print(service_total1_sum)
mask_service_total2 = service_total["분기"] == 2    # 음식서비스 2분기 마스크
service_total2 = service_total[mask_service_total2]    # 음식서비스 2분기만
service_total2_sum = service_total2['매출액'].sum()    #음식서비스 2분기 매출액 합
# print(service_total2)
# print(service_total2_sum)
mask_service_total3 = service_total["분기"] == 3    # 음식서비스 3분기 마스크
service_total3 = service_total[mask_service_total3]    # 음식서비스 3분기만
service_total3_sum = service_total3['매출액'].sum()    #음식서비스 3분기 매출액 합
# print(service_total3)
# print(service_total3_sum)
mask_service_total4 = service_total["분기"] == 4    # 음식서비스 4분기 마스크
service_total4 = service_total[mask_service_total4]    # 음식서비스 4분기만
service_total4_sum = service_total4['매출액'].sum()    #음식서비스 4분기 매출액 합
# print(service_total4)
# print(service_total4_sum)


# 농수축산물
food_total = stores19.query('상품명.str.contains("육류판매|청과상|미곡판매|수산물판매")', engine='python')    # 음식서비스 추출
# print(food_total)

mask_food_total1 = food_total["분기"] == 1    # 농수축산물 1분기 마스크
food_total1 = food_total[mask_food_total1]    # 농수축산물 1분기만
food_total1_sum = food_total1['매출액'].sum()    # 농수축산물 1분기 매출액 합
# print(food_total1)
# print(food_total1_sum)
mask_food_total2 = food_total["분기"] == 2    # 농수축산물 2분기 마스크
food_total2 = food_total[mask_food_total2]    # 농수축산물 2분기만
food_total2_sum = food_total2['매출액'].sum()    # 농수축산물 2분기 매출액 합
# print(food_total2)
# print(food_total2_sum)
mask_food_total3 = food_total["분기"] == 3    # 농수축산물 3분기 마스크
food_total3 = food_total[mask_food_total3]    # 농수축산물 3분기만
food_total3_sum = food_total3['매출액'].sum()    # 농수축산물 3분기 매출액 합
# print(food_total3)
# print(food_total3_sum)
mask_food_total4 = food_total["분기"] == 4    # 농수축산물 4분기 마스크
food_total4 = food_total[mask_food_total4]    # 농수축산물 4분기만
food_total4_sum = food_total4['매출액'].sum()    # 농수축산물 4분기 매출액 합
# print(food_total4)
# print(food_total4_sum)


# 스포츠, 레저
sports_total = stores19.query('상품명.str.contains("스포츠 강습|스포츠클럽|운동/경기용품|골프연습장")', engine='python')    # 음식서비스 추출
# print(sports_total)

mask_sports_total1 = sports_total["분기"] == 1    # 스포츠 1분기 마스크
sports_total1 = sports_total[mask_sports_total1]    # 스포츠 1분기만
sports_total1_sum = sports_total1['매출액'].sum()    # 스포츠 1분기 매출액 합
# print(sports_total1)
# print(sports_total1_sum)
mask_sports_total2 = sports_total["분기"] == 2    # 스포츠 2분기 마스크
sports_total2 = sports_total[mask_sports_total2]    # 스포츠 2분기만
sports_total2_sum = sports_total2['매출액'].sum()    # 스포츠 2분기 매출액 합
# print(sports_total2)
# print(sports_total2_sum)
mask_sports_total3 = sports_total["분기"] == 3    # 스포츠 3분기 마스크
sports_total3 = sports_total[mask_sports_total3]    # 스포츠 3분기만
sports_total3_sum = sports_total3['매출액'].sum()    # 스포츠 3분기 매출액 합
# print(sports_total3)
# print(sports_total3_sum)
mask_sports_total4 = sports_total["분기"] == 4    # 스포츠 4분기 마스크
sports_total4 = sports_total[mask_sports_total4]    # 스포츠 4분기만
sports_total4_sum = sports_total4['매출액'].sum()    # 스포츠 4분기 매출액 합
# print(sports_total4)
# print(sports_total4_sum)


# 새 데이터프레임
data = {'상품명': ['음,식료품', '음식서비스', '농수축산물', '스포츠, 레저'],
        '2019 1/4': [market_total1_sum, service_total1_sum, food_total1_sum, sports_total1_sum],
        '2019 2/4': [market_total2_sum, service_total2_sum, food_total2_sum, sports_total2_sum],
        '2019 3/4': [market_total3_sum, service_total3_sum, food_total3_sum, sports_total3_sum],
        '2019 4/4': [market_total4_sum, service_total4_sum, food_total4_sum, sports_total4_sum],}
df = pd.DataFrame(data)
df2 = df.set_index("상품명", drop=True)
# print(df)
print(df2)

# 시각화
plt.plot(df2.loc['음,식료품'], label="음,식료품")
plt.plot(df2.loc['음식서비스'], label="음식서비스")
plt.plot(df2.loc['농수축산물'], label="농수축산물")
plt.plot(df2.loc['스포츠, 레저'], label="스포츠, 레저")
plt.grid()
plt.legend()
plt.show()