import pandas as pd 
df = pd.read_csv('books.csv')
print(df.select_dtypes(include='object'))