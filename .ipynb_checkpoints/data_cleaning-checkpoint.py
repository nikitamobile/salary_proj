# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:12:18 2020

@author: n_baranov
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

df = df[df['Salary Estimate'] != '-1']