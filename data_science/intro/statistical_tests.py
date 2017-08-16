import pandas as pd
import numpy as np

import scipy.stats as st
from statsmodels.stats import weightstats as wst
from statsmodels.stats.proportion import proportions_chisquare as pchisq

df = pd.DataFrame({
        'age': [20, 25, 35, 31],
        'salary': [2500, 5000, 9500, 9000],
        'experience': [2, 4, 7, 4],
        'position': ['tester',  'tester', 'developer', 'developer']
        }, index=['person1', 'person2', 'person3', 'person4'])

df.age.plot(kind='bar')
df[['experience', 'salary']].plot(kind="scatter", x='experience', y='salary')

df[['position', 'salary']].boxplot(by='position')
df[['experience']].plot(kind='pie', subplots='True')


df2 = pd.DataFrame({
        'position': ['developer'] * 5 + ['tester'] * 5,
        'salary': [8500, 8000, 9200, 7700, 9900, 5200, 3200, 2000, 9000, 7700]
        
        })

st.ttest_ind(
        df2.salary[df2.position == 'developer'],
        df2.salary[df2.position == 'tester'],
        
        )

wst.ttest_ind( 
        df2.salary[df2.position == 'developer'],
        df2.salary[df2.position == 'tester'], 
        
        
        alternative='two-sided', 
        usevar='unequal')

df3 = pd.DataFrame({
        'high_school': [60, 40],
        'bachelors': [54, 44],
        'masters': [46, 53],
        'ph.d.': [41, 57]
        })

chi2_stat, pval, deg_fr, expected_counts = st.chi2_contingency(df3)
print("Chi2 stat: {0} \nPval: {1}\nDegr.free: {2}".format(
        chi2_stat, pval, deg_fr))

pchisq(df3)
