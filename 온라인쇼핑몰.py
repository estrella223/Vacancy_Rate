# 온라인 패턴

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
import warnings

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    online = pd.read_excel('온라인쇼핑몰_거래액.xlsx', engine='openpyxl')
# print(online.head())

online = online.query('범위별.str.contains("계")', engine='python')
# print(online.head())

online['2019.1/4'] = online['2019. 01'] + online['2019. 02'] + online['2019. 03']
online['2019.2/4'] = online['2019. 04'] + online['2019. 05'] + online['2019. 06']
online['2019.3/4'] = online['2019. 07'] + online['2019. 08'] + online['2019. 09']
online['2019.4/4'] = online['2019. 10'] + online['2019. 11'] + online['2019. 12']
online['2020.1/4'] = online['2020. 01'] + online['2020. 02'] + online['2020. 03']
online['2020.2/4'] = online['2020. 04'] + online['2020. 05'] + online['2020. 06']
online['2020.3/4'] = online['2020. 07'] + online['2020. 08'] + online['2020. 09']
online['2020.4/4'] = online['2020. 10'] + online['2020. 11'] + online['2020. 12']
online['2021.1/4'] = online['2021. 01'] + online['2021. 02'] + online['2021. 03']
online['2021.2/4'] = online['2021. 04'] + online['2021. 05 p)'] + online['2021. 06 p)']

online = online[['상품군별', '2019.1/4', '2019.2/4', '2019.3/4', '2019.4/4', '2020.1/4',
                 '2020.2/4', '2020.3/4', '2020.4/4', '2021.1/4', '2021.2/4']]
# print(online.head())
online = online.set_index("상품군별")

online2 = online.query('상품군별.str.contains("음·식료품|음식서비스|농축수산물|스포츠·레저용품")', engine='python')
print(online2)

plt.figure(figsize=(10, 6))
plt.plot(online2.loc["음·식료품"], label="음·식료품")
plt.plot(online2.loc["음식서비스"], label="음식서비스")
plt.plot(online2.loc["농축수산물"], label="농축수산물")
plt.plot(online2.loc['스포츠·레저용품'], label="스포츠·레저용품")

plt.grid(color= '#BDBDBD', alpha= 0.7)
plt.tick_params(direction= 'inout', length= 8, width=1)
plt.legend()
plt.show()

online2.to_csv('online매출액.csv', sep=',', na_rep='NaN')