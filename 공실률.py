# 공실률 변화추이(자료 by 이경덕)

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


empty_rate = pd.read_csv('mixdata19-21.csv', encoding='cp949')
empty_rate.rename(columns={'지역(소)': '지역'}, inplace=True)

#print(empty_rate.head())

# empty_rate = pd.merge(empty_rate.loc["홍대합정"], empty_rate.loc["홍대/합정"], on="지역")


print(empty_rate.sort_values(by='2021 02분기', ascending=False).head())

# 명동 이태원 홍대/합정 천호 성신여대

empty_rate = empty_rate.query('지역.str.contains("명동|이태원|홍대합정|천호|성신여대")', engine='python')
print(empty_rate)

empty_rate2 = empty_rate.set_index("지역")
print(empty_rate2)

plt.figure(figsize=(12, 6))
plt.plot(empty_rate2.loc["명동"], label="명동")
plt.plot(empty_rate2.loc["이태원"], label="이태원")
plt.plot(empty_rate2.loc["홍대합정"], label="홍대합정")
plt.plot(empty_rate2.loc["천호"], label="천호")
plt.plot(empty_rate2.loc["성신여대"], label="성신여대")

plt.legend()
plt.grid(color= '#BDBDBD', alpha= 0.7)
plt.tick_params(direction= 'inout', length= 8, width=1)
plt.show()
