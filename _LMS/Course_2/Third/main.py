import pandas as pd

"""
как я понял, нужно найти 2 разных группы людей, в случае если в задании требовалось
применять логический оператор И, то вывод будет пустым
"""
# возникла проблема с таблицей (заголовки слились в один заголовок) csv формата,
# поэтому я конвертировал таблицу в Excel формат
read_data = pd.read_excel('/content/Customers.xlsx')
df = pd.DataFrame(read_data)
query_df = df.loc[(df['Age'] > 30) & (df['Income'] < 30000) | (df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]


query_df
