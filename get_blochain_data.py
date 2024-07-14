# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:06:30 2022

@author: molaei
"""


import requests
import pandas as pd
import numpy as np
import json
import datetime
import time

#%%     Get Block Number by Timestamp
# url = "https://blockchain.info/rawblock/000000000000000000025fbc4f8ab866cbb0b122aa67ebc7cda06f20ea528c95"

url = "https://blockchain.info/latestblock"

def get_bno(url):
    res= requests.get(url)
    if res.ok :
            try:
                bno = pd.read_json(res.text)
            except:
                bno = json.loads(res.text)
                print("block no :",bno)
    else:
            print("Not Respons") 
    return bno

temp = get_bno(url)
print(temp)


# %%
