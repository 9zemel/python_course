import pandas as pd

dataFrame = pd.read_excel('Countries1.xls', sheet_name=0, header=1)

dataFrame.index = ['KZ', 'RU', 'BR']
# print(dataFrame.loc['KZ'])
# print(dataFrame.loc['KZ'].values[0])
#loc позволяет выбирает по индексу

# print(dataFrame.iloc[1].values[0])
dataFrame.index.name = 'Коды доступа первого уровня'

print(dataFrame.loc[['BR'],'Population'])
