import pymysql
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://tripleS:ssafy@k3b205.p.ssafy.io:3306/triples_data", encoding='utf-8-sig')

# 1
table = pd.read_excel('perfumes.xlsx')
table.to_sql(name='perfumes_perfume', con=engine,
             if_exists='append', index=False)
