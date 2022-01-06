import pandas as pd
import matplotlib.pyplot as plt

'''파일 불러오기'''
seouldf = pd.read_csv('서울 업종별 점포 매출 통계(2020.02)_20210815.csv')
seouldf = pd.DataFrame(seouldf)
seouldf = seouldf.drop(seouldf[['광역시도']],axis = 1)
seouldf = seouldf.set_index(['년도','월'],drop= True)
#
# daegudf = pd.read_csv('대구 업종별 점포 매출 통계(2020.02)_20210815.csv')
# daegudf = pd.DataFrame(daegudf)
# daegudf = daegudf.set_index(['년도','월'],drop= True)
#
# daejundf = pd.read_csv('대전 업종별 점포 매출 통계(2020.02)_20210815.csv')
# daejundf = pd.DataFrame(daejundf)
# daejundf = daejundf.set_index(['년도','월'],drop= True)
#
# busandf = pd.read_csv('부산 업종별 점포 매출 통계(2020.02)_20210815.csv')
# busandf = pd.DataFrame(busandf)
# busandf = busandf.set_index(['년도','월'],drop= True)
# #
# ulsandf = pd.read_csv('서울 업종별 점포 매출 통계(2020.02)_20210815.csv')
# ulsandf = pd.DataFrame(ulsandf)
# ulsandf = ulsandf.set_index(['년도','월'],drop= True)
#
#
#

'''업종 필터 - 서울 '''
foodstore1 = seouldf.query('업종.str.contains("닭/오리요리|분식|한식|중식|커피/음료")', engine = 'python')
foodstore2 = seouldf.query('업종.str.contains("미용서비스|화장품소매")', engine = 'python')
foodstore3 = seouldf.query('업종.str.contains("의복/의류")', engine = 'python')
foodstore4 = seouldf.query('업종.str.contains("일반병원")', engine = 'python')
foodstore5 = seouldf.query('업종.str.contains("입시학원")', engine = 'python')
'''분기별 합산'''

foodstore1_0 = foodstore1[foodstore1['업종'] == '닭/오리요리']
data1 = foodstore1_0[:2].sum(axis=0)
data2 = foodstore1_0[2:6].sum(axis=0)
data3 = foodstore1_0[6:10].sum(axis=0)
data4 = foodstore1_0[10:12].sum(axis=0)

foodstore1_1 = foodstore1[foodstore1['업종'] == '분식']
ndata1 = foodstore1_1[:2].sum(axis=0)
ndata2 = foodstore1_1[2:6].sum(axis=0)
ndata3 = foodstore1_1[6:10].sum(axis=0)
ndata4 = foodstore1_1[10:12].sum(axis=0)

kfoodstore1_2 = foodstore1[foodstore1['업종'] == '한식']
kdata1 = kfoodstore1_2[:2].sum(axis=0)
kdata2 = kfoodstore1_2[2:6].sum(axis=0)
kdata3 = kfoodstore1_2[6:10].sum(axis=0)
kdata4 = kfoodstore1_2[10:12].sum(axis=0)

cfoodstore1_3 = foodstore1[foodstore1['업종'] == '중식']
cdata1 = cfoodstore1_3[:2].sum(axis=0)
cdata2 = cfoodstore1_3[2:6].sum(axis=0)
cdata3 = cfoodstore1_3[6:10].sum(axis=0)
cdata4 = cfoodstore1_3[10:12].sum(axis=0)

lfoodstore1_4 = foodstore1[foodstore1['업종'] == '커피/음료']
ldata1 = lfoodstore1_4[:2].sum(axis=0)
ldata2 = lfoodstore1_4[2:6].sum(axis=0)
ldata3 = lfoodstore1_4[6:10].sum(axis=0)
ldata4 = lfoodstore1_4[10:12].sum(axis=0)

lfoodstore2_1= foodstore2[foodstore2['업종'] == '미용서비스']
mdata1 = lfoodstore2_1[:2].sum(axis=0)
mdata2 = lfoodstore2_1[2:6].sum(axis=0)
mdata3 = lfoodstore2_1[6:10].sum(axis=0)
mdata4 = lfoodstore2_1[10:12].sum(axis=0)

lfoodstore2_2= foodstore2[foodstore2['업종'] == '화장품소매']
ldata5 = lfoodstore2_2[:2].sum(axis=0)
ldata6 = lfoodstore2_2[2:6].sum(axis=0)
ldata7 = lfoodstore2_2[6:10].sum(axis=0)
ldata8 = lfoodstore2_2[10:12].sum(axis=0)

foodstore3_1= foodstore3[foodstore3['업종'] == '의복/의류']
ydata1 = foodstore3_1[:2].sum(axis=0)
ydata2 = foodstore3_1[2:6].sum(axis=0)
ydata3 = foodstore3_1[6:10].sum(axis=0)
ydata4 = foodstore3_1[10:12].sum(axis=0)

foodstore4_1= foodstore4[foodstore4['업종'] == '일반병원']
hdata1 = foodstore4_1[:2].sum(axis=0)
hdata2 = foodstore4_1[2:6].sum(axis=0)
hdata3 = foodstore4_1[6:10].sum(axis=0)
hdata4 = foodstore4_1[10:12].sum(axis=0)

foodstore5_1= foodstore5[foodstore5['업종'] == '입시학원']
adata1 = foodstore5_1[:2].sum(axis=0)
adata2 = foodstore5_1[2:6].sum(axis=0)
adata3 = foodstore5_1[6:10].sum(axis=0)
adata4 = foodstore5_1[10:12].sum(axis=0)

new_data = {'업종': ['음식', '미용', '의복/의류', '일반병원','입시학원'],
            '2019 2/4' : [data1[1]+ndata1[1]+kdata1[1]+cdata1[1]+ldata1[1],mdata1[1]+ldata5[1],ydata1[1],hdata1[1],adata1[1]],
            '2019 3/4' : [data2[1]+ndata2[1]+kdata2[1]+cdata2[1]+ldata1[1],mdata2[1]+ldata6[1],ydata2[1],hdata2[1],adata2[1]],
            '2019 4/4' : [data3[1]+ndata3[1]+kdata3[1]+cdata3[1]+ldata1[1],mdata3[1]+ldata7[1],ydata3[1],hdata3[1],adata3[1]],
            '2020 1/4' : [data4[1]+ndata4[1]+data4[1]+cdata4[1]+ldata1[1],mdata4[1]+ldata8[1],ydata4[1],hdata4[1],adata4[1]]}
new_data = pd.DataFrame(new_data)
new_data = new_data.set_index(['업종'],drop=True)
new_data.to_csv('서울시 음식업종 분기별 합산.csv')
print(new_data)

'''그래프세팅'''
# plt.rcParams['font.family'] = 'Malgun Gothic'
# # plt.title("서울시 음식")
# plt.xlabel('월별')
# plt.ylabel('매출')
# plt.rc('font',size = 5)
# plt.xticks(size= 5)
# plt.yticks(size=5)
#

'''그래프그리기 - 서울 '''
# new_data.plot(label = '닭,오리')
# foodstore2['값(만)'].plot(label = '분식')
# foodstore3['값(만)'].plot(label = '한식')
# foodstore4['값(만)'].plot(label = '중식')

# plt.legend()
# plt.show()