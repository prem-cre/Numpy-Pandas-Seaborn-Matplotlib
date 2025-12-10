import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.boxplot(y='Total',data=mart,width=0.2)
# plt.show()
##########

# sns.boxplot(x='Payment',y='Total',data=mart)
# plt.show()
##########

# sns.boxplot(x='Payment',y='Total',hue='Gender',data=mart,showmeans=True,meanprops={"marker":'o',
#             'markerfacecolor':'white','markersize':'5','markeredgecolor':'black'},palette='CMRmap'
#                                                     ,linewidth=5)
# plt.show()

####### box plot for each value

plt.figure(figsize=(15,5))
sns.boxplot(data=mart)
plt.show()










