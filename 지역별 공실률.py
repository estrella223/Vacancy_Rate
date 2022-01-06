import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''도시별 공실률 파일 불러오기_소규모2019'''
# stores19_s = pd.read_excel('지역별공실률_소규모_상가_신표본(2019년 이후)_개정.xlsx', skiprows=3,skipfooter=160)
# dfstores19_s = pd.DataFrame(stores19_s)
# dfstores19_s.columns= ['도시','지역(중)','지역(소)','2019 01분기','2019 02분기','2019 03분기','2019 04분기']
#
# idx = dfstores19_s[dfstores19_s['지역(소)'] == '전체'].index
# dfstores19_s = dfstores19_s.drop(idx)
#
# dfstores19_s = dfstores19_s.set_index(['지역(소)'],drop=True)
# dfstores19_s.drop(['도시','지역(중)'],axis = 1, inplace=True)
# dfstores19_s.to_csv('dfstores19_s.csv')
# # print(dfstores19_s)

'''서울 공실률 파일 불러오기_소규모2020'''
# stores20_s = pd.read_excel('지역별공실률_소규모_상가_신표본(2020년 이후)_개정.xlsx', skiprows=3,skipfooter=174,)
# dfstores20_s = pd.DataFrame(stores20_s)
# dfstores20_s.columns= ['도시','지역(중)','지역(소)','2020 01분기','2020 02분기','2020 03분기','2020 04분기']
#
# idx = dfstores20_s[dfstores20_s['지역(소)'] == '전체'].index
# dfstores20_s = dfstores20_s.drop(idx)
# dfstores20_s = dfstores20_s.set_index(['지역(소)'],drop=True)
# dfstores20_s.drop(['도시','지역(중)'],axis = 1, inplace=True)
# dfstores20_s.to_csv('dfstores20_s.csv')

'''서울 공실률 파일 불러오기_2020'''
stores21_s = pd.read_excel('지역별공실률_소규모_상가_신표본(2021년 이후)_개정.xlsx', skiprows=3,skipfooter=185)
dfstores21_s = pd.DataFrame(stores21_s)
dfstores21_s.columns= ['도시','지역(중)','지역(소)','2021 01분기','2021 02분기']

idx = dfstores21_s['도시'].fillna(value='서울',inplace=True)
idx2 = dfstores21_s['지역(중)'][:7].fillna(value='도심',inplace=True)
idx3 = dfstores21_s['지역(중)'][:18].fillna(value='강남',inplace=True)
idx4 = dfstores21_s['지역(중)'][:26].fillna(value='영등포신촌',inplace=True)
idx5 = dfstores21_s['지역(중)'][:56].fillna(value='기타',inplace=True)
idx_del = dfstores21_s.dropna(how='any',inplace=True)
dfstores21_s.drop(['도시','지역(중)'],axis = 1, inplace=True)
dfstores21_s = dfstores21_s.set_index(['지역(소)'],drop=True)
dfstores21_s.to_csv('dfstores21_s.csv')


'''고은누나 자료'''
# dfother19 = pd.read_excel('2020공실률.xlsx')
# dfother19 = pd.DataFrame(dfother19)
# # dfother19.drop(['광역상권','임대료','투자수익률','소득수익률','자본수익률'],axis = 1, inplace=True)
# # dfother19.set_index(['기간'],drop=True)
# # print(dfother19)
# data = {'지역(소)': dfother19['하위상권'][3:56]}
# data1 = {'2020 01분기': dfother19['공실률'][3:56]}
# data2 = {'2020 02분기': dfother19['공실률'][58:111]}
# data3 = {'2020 03분기': dfother19['공실률'][113:166]}
# data4 = {'2020 04분기': dfother19['공실률'][168:221]}
#
# data = pd.DataFrame(data)
# df1 = data.reset_index(drop=True)
#
# data1 = pd.DataFrame(data1)
# df2 = data1.reset_index(drop=True)
#
# data2 = pd.DataFrame(data2)
# df3 = data2.reset_index(drop=True)
#
# data3 = pd.DataFrame(data3)
# df4 = data3.reset_index(drop=True)
#
# data4 = pd.DataFrame(data4)
# df5 = data4.reset_index(drop=True)
#
#
# ddata = pd.concat([df1,df2,df3,df4,df5],axis=1)
#
# ddata.to_csv('data20.csv')
# print(ddata)

'''공실률 합치기'''
dfstores19 = pd.read_csv('dfstores19_s.csv')
dfstores19 = pd.DataFrame(dfstores19)
dfstores19 = dfstores19.set_index(['지역(소)'],drop=True)

dfstores20 = pd.read_csv('dfstores20_s.csv')
dfstores20 = pd.DataFrame(dfstores20)
dfstores20 = dfstores20.set_index(['지역(소)'],drop=True)

dfstores21 = pd.read_csv('dfstores21_s.csv')
dfstores21 = pd.DataFrame(dfstores21)
dfstores21.at[23,['지역(소)']] = '홍대합정'
dfstores21.at[19,['지역(소)']] = '동교연남'
dfstores21.at[21,['지역(소)']] = '신촌이대'
dfstores21.at[29,['지역(소)']] = '독산시흥'
dfstores21.at[46,['지역(소)']] = '잠실송파'
# print(dfstores21)
dfstores21 = dfstores21.set_index(['지역(소)'], drop=True)


dfother19 = pd.read_csv('data19.csv')
idx = dfother19[dfother19['지역(소)'] == '소계'].index
dfother19 = dfother19.drop(idx)
dfother19 = dfother19.set_index(['지역(소)'],drop=True)
dfother19 = pd.DataFrame(dfother19)

dfother20 = pd.read_csv('data20.csv')
idx = dfother20[dfother20['지역(소)'] == '소계'].index
dfother20 = dfother20.drop(idx)
dfother20 = dfother20.set_index(['지역(소)'],drop=True)
dfother20 = pd.DataFrame(dfother20)


dfother21 = pd.read_csv('data21.csv')
idx = dfother21[dfother21['지역(소)'] == '소계'].index
dfother21 = dfother21.drop(idx)
dfother21 = dfother21.set_index(['지역(소)'],drop=True)
dfother21 = pd.DataFrame(dfother21)


mixes = pd.concat([dfstores19,dfstores20,dfstores21],axis=1,join='outer')
ddata = dfother19.join(dfother20, how='outer')
ddata1 = ddata.join(dfother21,how='outer')

# ddata1.to_csv('ddes.csv')
# print(ddata1)
take_bigger = lambda s1, s2: s1 if s1.sum() > s2.sum() else s2
# result1 = mixes.combine(ddata1, take_bigger)
result1 = mixes.combine(ddata1, np.maximum)
result = result1.dropna(axis=0, how = 'any')
result = result.sort_values(by='2020 01분기',ascending=False)
result = result.head(10)
print(result)


plt.rcParams['font.family'] = 'Malgun Gothic'
for i in result.index:
    plt.plot(result.loc[i], label = i)



plt.title("서울시 상가공실률")
plt.xlabel('년도 별 추이(분기 단위)')
plt.ylabel('공실률(%)')
plt.rc('font',size = 5)
plt.xticks(size= 5)
plt.yticks(size=5)
plt.legend()
plt.show()