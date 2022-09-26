import pandas as pd

df = pd.read_csv('PSRA.csv')
trou = 1878
trou2 = 1879
a = df.loc[(df['pm2.5'].isnull()) & (df['No'] == trou)]
a2 = df.loc[(df['pm2.5'].isnull()) & (df['No'] == trou2)]

b = df.loc[(df['No'] == trou-1)]
b2 = df.loc[(df['No'] == trou2+1)]

print(b)
print(b2)
c = int(b['pm2.5'])
c2 = int(b2['pm2.5'])
print(abs(c2-c))