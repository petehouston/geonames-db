import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('./data/US.txt', sep='\t', names=['country', 'postal_code', 'name', 'state_name', 'state_code',
                                                   'county_name', 'county_code', 'comm_name', 'comm_code',
                                                   'latitude', 'longitude', 'accuracy'])

engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/')

df.to_sql('geocodes', con=engine, if_exists='replace', schema='geo_db', index_label='id', chunksize=100)

print('DONE!')
