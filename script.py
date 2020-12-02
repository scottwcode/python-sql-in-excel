import sqlite3
import pandas as pd
from sqlalchemy import create_engine
# file = 'testfile.xls'
file = 'testfile.xlsx'
output = 'output.xlsx'
engine = create_engine('sqlite://', echo=False)
df = pd.read_excel(file, sheet_name='2018-12-29-bbs-listings')
df.to_sql('listings', engine, if_exists='replace', index=False)

# results = engine.execute("Select * from listings")
# results = engine.execute("Select * from listings where pe>2")
# results = engine.execute("Select * from listings where state='OK'")
results = engine.execute("Select * from listings where name LIKE 'Biz%'")

final = pd.DataFrame(results, columns=df.columns)
final.to_excel(output, index=False)

final

