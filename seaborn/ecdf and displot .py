import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')
mart=mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)

sns.ecdfplot(data=mart,x='gross income',hue='Gender',stat='count')
plt.show()















