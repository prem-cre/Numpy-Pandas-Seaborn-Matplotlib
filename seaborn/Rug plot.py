import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')
mart=mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)

# plt.figure(figsize=(15,5))
# sns.rugplot(data=mart,x='Unit price',y='gross income',hue='Gender',height=0.09)
# plt.show()
######

# plt.figure(figsize=(15,5))
# sns.rugplot(data=mart,x='Unit price',y='gross income',hue='Gender')
# sns.kdeplot(data=mart,x='Unit price',y='gross income',hue='Gender',fill=True)
# plt.show()
##########

# plt.figure(figsize=(15,5))
# sns.rugplot(data=mart,x='Unit price',y='gross income',hue='Gender')
# sns.scatterplot(data=mart,x='Unit price',y='gross income',hue='Gender')
# plt.show()
#############

plt.figure(figsize=(15,5))
sns.rugplot(data=mart,x='Unit price',y='gross income',hue='Gender',height=-0.01,clip_on=False)
sns.kdeplot(data=mart,x='Unit price',y='gross income',hue='Gender',fill=True)
plt.show()







