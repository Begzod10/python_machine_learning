import pandas as pd
import numpy as np

from sqlalchemy import create_engine

# temp_db = create_engine('sqlite:///:memory:')
engine = create_engine(
    "postgresql://postgres:123@localhost/gennis",
    isolation_level="REPEATABLE READ"
)
# df = pd.DataFrame(data=np.random.randint(low=0, high=100, size=(4, 4)), columns=['a', 'b', 'c', 'd'])
# df.to_sql(name='gennis2.sql', con=temp_db, schema='online_test', index=False, if_exists='append')
# print(df)
new_df = pd.read_sql(sql='SELECT name,img, price FROM book', con=engine)
print(new_df)
