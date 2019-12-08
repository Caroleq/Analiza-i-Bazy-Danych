import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import plotnine as p9


df = pd.read_csv('exercise.csv')

results = smf.ols('y ~ x1 + x2 + x1*x2', data=df).fit()

wyn=results.params

print(results.summary())


fig1=(p9.ggplot(p9.aes(x='x1,x2',y='y'),data=df)+p9.geom_jitter(width=0.1)
      +p9.geom_abline(p9.aes(intercept=wyn['Intercept'],slope=wyn['x1'])))


plt.show()
