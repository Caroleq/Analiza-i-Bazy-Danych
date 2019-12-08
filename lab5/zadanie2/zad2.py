import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('earthquake_data.csv')

earth_big = 'How worried are you about the Big One, a massive, catastrophic earthquake?'
earth_gen = 'In general, how worried are you about earthquakes?'
money = 'How much total combined money did all members of your HOUSEHOLD earn last year?'
gender = 'What is your gender?'
reg = 'US Region'
exp = 'How familiar are you with the Yellowstone Supervolcano?'

df.groupby([reg, earth_big])[reg].count().unstack().reset_index().plot.bar(x = reg)
df.groupby([reg, earth_gen])[reg].count().unstack().reset_index().plot.bar(x = reg)

df.groupby([gender, earth_big])[gender].count().unstack().reset_index().plot.bar(x = gender)
df.groupby([gender, earth_gen])[gender].count().unstack().reset_index().plot.bar(x = gender)

df.groupby([money,exp])[money].count().unstack().reset_index().plot.bar(x = money)
plt.show()
