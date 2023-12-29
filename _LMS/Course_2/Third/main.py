import pandas as pd

read_data = pd.read_csv('/content/Customers.csv', sep=";")
df = pd.DataFrame(read_data)
query_df = df.loc[(df['Age'] > 30) & (df['Income'] < 30000) | (df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]


query_df
