import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.jointplot(data=mart,y='Total',x='Payment',kind='scatter')
# plt.show()                                          #kind=scatter,hist,kde,hex,reg,resid
########

# sns.jointplot(data=mart,x='Total',y='Rating',hue='Customer type')
# plt.show()
########

# sns.jointplot(data=mart,x='Total',y='Rating',joint_kws=dict(marker='*',color='red')
#               ,marginal_kws=dict(color='green',kde=True))
# plt.show()
########

# sns.jointplot(data=mart,x='Total',y='Rating',height=4,                     #use space =5
#               ratio=2,marginal_ticks=True)
# plt.show()
############

l=sns.jointplot(data=mart,x='Total',y='Rating',color='r')
l.plot_joint(sns.kdeplot)
l.plot_joint(sns.rugplot,height=0.05)
plt.show()












