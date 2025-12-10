import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.violinplot(y='Total',data=mart)
# plt.show()
#######

# sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True)
# plt.show()
##########

# sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='box',bw=.2)
# plt.show()                                                  # inner=quartile,stick,box
#############

sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='box',cut=0)
plt.show()

