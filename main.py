import csv

import pandas as pd

df1 = pd.read_csv('dwarf_stars.csv')
df2 = pd.read_csv('bright_stars.csv')

headers = ['Star_name','Distance','Mass','Radius']

df1_clean = pd.DataFrame()
df2_clean = pd.DataFrame()

for header in headers:
    df1_clean[header] = df1[header]
    df2_clean[header] = df2[header]

df1_clean = df1_clean.dropna()
df2_clean = df2_clean.dropna()

print(df1_clean.head())
print(df2_clean.head())

#df1_clean['Mass'] = 0.000954588 * float(df1_clean['Mass'])
#df1_clean['Radius'] = 0.102763 * float(df1_clean['Radius'])

result = pd.concat([df1_clean, df2_clean])

result.to_csv('all_stars.csv', index=False)
