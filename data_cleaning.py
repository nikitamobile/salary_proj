# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:12:18 2020

@author: n_baranov
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

df = df[df['Salary Estimate'] != '-1']


#Salary parsing
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K',' ').replace('$',''))

df['min_salary'] = minus_kd.apply(lambda x: int(x.split(' ')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split(' ')[1].replace('-', '')))
df['avg_salary'] = (df.max_salary + df.min_salary)/2
df['monthly_wage'] = df.avg_salary / 12

#Company name cleaning

df['company_txt'] = df.apply(lambda x: x['Company Name'][:-3], axis = 1)
