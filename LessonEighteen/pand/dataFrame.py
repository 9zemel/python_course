import pandas as pd

dataFrame = pd.read_csv('Countries.csv', sep = ',')
print(dataFrame.head)

dataFrame.index = ['KZ', 'RU', 'BR', 'UK']
print(dataFrame.head(5))

dataFrame.index.name = 'Коды доступа первого уровня'

print(dataFrame.loc[['BR'],'Square'])
