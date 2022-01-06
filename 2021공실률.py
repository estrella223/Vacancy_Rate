import pandas as pd
import matplotlib.pyplot as plt


empty_rate21 = pd.read_csv('2021공실률.csv', encoding='cp949')
# print(empty_rate.head())

empty_rate21.rename(columns={'기간': '분기'}, inplace=True)
empty_rate21.drop([0], inplace=True)
# print(empty_rate.head())

empty_rate21 = empty_rate21[['하위상권', '분기', '공실률']]
# print(empty_rate.head())

# empty_rate19 = empty_rate19.astype({'공실률': 'float'})

empty_rate21 = empty_rate21.query('하위상권.str.contains("명동|광화문|논현역|테헤란로|이태원")',
                         engine='python')

print(empty_rate21.sort_values(by=('하위상권'), ascending=True))