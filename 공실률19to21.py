# 공실률 변화 추이(자료 by 추고은)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


empty_rate19 = pd.read_excel('2019공실률.xlsx')
empty_rate19.rename(columns={'기간': '분기'}, inplace=True)
empty_rate19.drop([0], inplace=True)

empty_rate20 = pd.read_excel('2020공실률.xlsx')
empty_rate20.rename(columns={'기간': '분기'}, inplace=True)
empty_rate20.drop([0], inplace=True)

empty_rate21 = pd.read_csv('2021공실률.csv', encoding='cp949')
empty_rate21.rename(columns={'기간': '분기'}, inplace=True)
empty_rate21.drop([0], inplace=True)

merge_rate = pd.concat([empty_rate19, empty_rate20, empty_rate21])
print(merge_rate)

mask_gwang = merge_rate["하위상권"] == "광화문"
mask_gwang = merge_rate[mask_gwang]
mask_myeong = merge_rate["하위상권"] == "명동"
mask_myeong = merge_rate[mask_myeong]
mask_non = merge_rate["하위상권"] == "논현역"
mask_non = merge_rate[mask_non]
mask_te = merge_rate["하위상권"] == "테헤란로"
mask_te = merge_rate[mask_te]
mask_yi = merge_rate["하위상권"] == "이태원"
mask_yi = merge_rate[mask_yi]

gwang_x = mask_gwang['분기']
gwang_y = mask_gwang['공실률']
myeong_x = mask_myeong['분기']
myeong_y = mask_myeong['공실률']
non_x = mask_non['분기']
non_y = mask_non['공실률']
te_x = mask_te['분기']
te_y = mask_te['공실률']
yi_x = mask_yi['분기']
yi_y = mask_yi['공실률']

plt.figure(figsize=(10, 6))
plt.title("2019 ~ 2021 공실률 변화 추이")
plt.plot(gwang_x, gwang_y, label='광화문')
plt.plot(myeong_x, myeong_y, label='명동')
plt.plot(non_x, non_y, label='논현역')
plt.plot(te_x, te_y, label='테헤란로')
plt.plot(yi_x, yi_y, label='이태원')
plt.xlabel("분기")
plt.ylabel("공실률")
plt.grid(color= '#BDBDBD', alpha= 0.7)
plt.tick_params(direction= 'inout', length= 8, width=1)
plt.legend()
plt.show()