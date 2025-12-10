import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.swarmplot(y='Total',data=mart)
# plt.show()
##########

# sns.swarmplot(y='Total',x='Payment',data=mart,hue='Gender',dodge=True,marker='*',size=10,edgecolor='black')
# plt.show()                                              #dodge or split
##########

# sns.swarmplot(y='Total',x='Payment',data=mart,hue='Gender',dodge=True)
# plt.show()
######

sns.swarmplot(y='Total',x='Payment',data=mart,hue='Gender',dodge=True)
sns.boxplot(y='Total',x='Payment',data=mart)
plt.show()



















