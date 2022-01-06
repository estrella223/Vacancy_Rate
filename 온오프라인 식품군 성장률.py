import pandas as pd
import matplotlib.pyplot as plt

onoff= pd.read_csv('산업통상자원부_주요 유통업체 26개사 온오프라인 식품군 월간 전년동기대비 성장률_20210630.csv',
                   encoding= '949', skiprows=42, skipfooter=13)

onoff = pd.DataFrame(onoff)
onoff.columns = ['년월', '오프라인_13개사_전년동월대비_성장률','온라인_13개사_전년동월대비_성장률', '전체_전체성장률']
onoff = onoff[['년월', '오프라인_13개사_전년동월대비_성장률','온라인_13개사_전년동월대비_성장률']]
new_onoff = onoff.set_index(['년월'],drop= True)
print(new_onoff)

plt.rcParams['font.family'] = 'Malgun Gothic'

new_onoff.plot()
plt.rc('font',size = 5)
plt.xticks(size= 5)
plt.yticks(size=5)
plt.legend()
plt.show()