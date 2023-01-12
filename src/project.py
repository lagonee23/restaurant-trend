import pandas as pd
import sqlite3

df = pd.read_csv('src/dine_out_seoul_202210.csv', encoding='cp949')
print(df.head())