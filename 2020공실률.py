import pandas as pd
import matplotlib.pyplot as plt

empty_rate20 = pd.read_excel('2020공실률.xlsx')
# print(empty_rate.head())

empty_rate20.rename(columns={'기간': '분기'}, inplace=True)
empty_rate20.drop([0], inplace=True)
# print(empty_rate.head())

empty_rate20 = empty_rate20[['하위상권', '분기', '공실률']]
# print(empty_rate.head())

# empty_rate19 = empty_rate19.astype({'공실률': 'float'})

empty_rate20 = empty_rate20.query('하위상권.str.contains("명동|광화문|논현역|테헤란로|이태원")',
                         engine='python')

print(empty_rate20.sort_values(by=('하위상권'), ascending=True))