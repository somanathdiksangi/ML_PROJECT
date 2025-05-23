import os 
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql



load_dotenv()
host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')


def read_sql_data():
    logging.info("reading from myaql started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connextion good",mydb)
        df=pd.read_sql_query('select * from raw',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex)


