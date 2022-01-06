import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

'''파일 불러오기'''
seouldf = pd.read_csv('서울시 우리마을가게 상권분석서비스(상권-추정매출)_2019.csv',encoding = 'cp949')
seouldf = pd.DataFrame(seouldf)
# print(seouldf)

'''필요한 열만 쓰도록 자르기'''
need_name = seouldf.iloc[:,[0,1,7,8]]
need_name = need_name.set_index(['기준_년_코드'],drop= True)
# need_name.index.name="업종"
need_name= need_name.sort_values(by = '기준_분기_코드',ascending=True)
# print(need_name)

'''특정 업종만 보기(마스크 씌우기) - 음식서비스'''
foodserv = need_name.query('서비스_업종_코드_명.str.contains("반찬가게|분식전문점|양식음식점|일식음식점|제과점|중식음식점|치킨전문점|커피-음료|패스트푸드점|한식음식점")', engine='python')
foodstore = need_name.query('서비스_업종_코드_명.str.contains("슈퍼마켓|편의점")', engine = 'python')
farm = need_name.query('서비스_업종_코드_명.str.contains("청과상|육류판매|수산물판매|미곡판매")', engine = 'python')
sports = need_name.query('서비스_업종_코드_명.str.contains("스포츠 강습|스포츠클럽|운동/경기용품|골프연습장")', engine = 'python')

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
    return sellall

# new DataFrame
data = {'분기별': ['2019 1/4', '2019 2/4', '2019 3/4', '2019 4/4'],
        '음식료품': findcell(foodstore),
        '음식서비스': findcell(foodserv),
        '농수축산물': findcell(farm),
        '스포츠,레저': findcell(sports)}
df = pd.DataFrame(data)
df2 = df.set_index("분기별", drop=True)
print(df2)

df2.plot()
plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))
plt.grid(color= '#BDBDBD', alpha= 0.7)
plt.legend(loc='center right')    # bbox_to_anchor=(1, 0.5), ncol=2
plt.tick_params(direction= 'inout', length= 8, width=1) # width=0
plt.title('2019 오프라인 매출액', fontsize=20)
plt.show()