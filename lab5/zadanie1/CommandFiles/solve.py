import pandas as pd
from io import StringIO
import operator


columns = ['id', 'year', 'month', 'element', *[str(i).zfill(2) for i in range (1, 32)]]

with open('weather.txt') as weathertxt, open('weather.csv', 'w') as weathercsv:
    csv = []
    for line in weathertxt.readlines():
        newline = line[:11] + ', ' + line[11:15] + ',' +  line[15:17] + ',' + line[17:21] + ', ' + line[21:].strip('\n')
        newline = newline.replace('S', ',')
        newline = newline.replace('I ', ', ')
        newline = newline.replace(' I', '')
        newline = newline.replace('-9999', ',')
        newline.strip(',')
        csv.append(newline)

    csv = '\n'.join(csv)
    weathercsv.write(csv)

df = pd.read_csv(StringIO(csv), header=None, sep=',', error_bad_lines=False, warn_bad_lines=False, names=columns)

df = pd.melt(df, id_vars=['id', 'year', 'month', 'element'], value_vars=[str(i) .zfill(2) for i in range (1, 32)])

df['year'] = df['year'].astype(str) + '-'
df['month'] = df['month'].astype(str) + '-'  
df['month'] = df['month'].apply(lambda x: '{0:0>3}'.format(x))
df['date'] = df['year'] + df['month'] + df['variable']
df.drop('year', axis=1, inplace=True)
df.drop('month', axis=1, inplace=True)
df.drop('variable', axis=1, inplace=True)

lookup = df.drop_duplicates('date')
lookup.drop('element', axis=1, inplace=True)
lookup.drop('value', axis=1, inplace=True)
lookup.set_index(['date'], inplace=True, drop=False)

df = df.pivot(columns='element', values='value', index='date')
df = df.join(lookup)
df = df.reset_index(drop=True)
df.sort_values(by=["date"], inplace=True)
    
cols = ['id', 'date', 'PRCP', 'TMIN', 'TMAX']
df = df[cols]
    
df.to_csv('tidy.csv', sep=',', index=False)

