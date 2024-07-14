# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:19:58 2022

@author: molaei
"""

import psycopg2
from configparser import ConfigParser

def config(filename='conf.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
    
class connection():
    def __init__(self, params = config()):
        super().__init__()
    
    def connect():
        params = config()
        conn=None
        try:
            conn= psycopg2.connect(**params)
            print("Connection to database succeeded...")
            conn.close()
        except:
            print("!!!Connection to database unsucceeded !!!")
            conn.rollback()
    
    # creat table
    def create_tables(flag):
        conn = None
        if flag == 0: #creat table for block
            commands = (
            """
            CREATE TABLE block (
                block_index SERIAL PRIMARY KEY,
                hash VARCHAR(70) NOT NULL,
                size integer NOT NULL,
                merkle VARCHAR(70) NOT NULL,
                
                
            )
            """)   
        elif flag == 1: #creat table for transaction
            commands = (
            """
            CREATE TABLE transaction (
                TRX_id BIGSERIAL PRIMARY KEY,
                TRX_hash VARCHAR(70) NOT NULL,
                TRX_HM REAL NOT NULL,
                TRX_type VARCHAR(32) NOT NULL
            )
            """)  
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(commands)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            if conn is not None:
                conn.close()
    
    
