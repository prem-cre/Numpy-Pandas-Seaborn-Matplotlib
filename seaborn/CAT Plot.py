import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')


# sns.catplot(data=mart,x='Payment',y='Total',col='Gender',kind='violin')
sns.catplot(data=mart,x='Payment',y='Total',col='Gender',kind='violin',row='Customer type')
plt.show()























