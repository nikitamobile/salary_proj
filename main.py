# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:28:01 2020

@author: n_baranov
"""

import pandas as pd
import glassdoor_scraper as gs

#path = r'C:\Users\user03\Documents\chromedriver\chromedriver.exe'
path = r'D:\Niki\Data Science\salary_proj\salary_proj\chromedriver_win32\chromedriver.exe'
slp_time=15

df = gs.get_jobs('data scientist', 99, False, path, slp_time)


df.to_csv('glassdoor_jobs.csv', index = False)
