import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx').sample(100)
mart.head()

# sns.relplot(data=mart,x='Payment',y='Total',kind='line',ci=None,hue='Gender',col='Product line',col_wrap=4)
# plt.show()                                                                              # ci or errorbar
###########

sns.relplot(data=mart,x='Payment',y='Total',kind='line',hue='Gender',col='Product line',row='Customer type',ci=None)
plt.show()

















