import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')
mart=mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)

# sns.kdeplot(data=mart,x='Total',bw_adjust=0.2)
# plt.show()

# sns.kdeplot(data=mart,hue='Payment',multiple='stack',log_scale=True,linewidth=5,)
# plt.show()
#########

sns.kdeplot(data=mart,x='Unit price',y='gross income',hue='Gender',fill=True,levels=5,thresh=0.2)
plt.show()













