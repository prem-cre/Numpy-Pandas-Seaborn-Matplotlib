import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.stripplot(y='Total',data=mart)
# plt.show()
############

# sns.stripplot(y='Total',data=mart,jitter=2)
# plt.show()
#########

# sns.stripplot(y='Total',x='Payment',hue='Gender',data=mart,linewidth=0.9,jitter=0.2,dodge=True)
# plt.show()                                      # dodge seprates male nad female

# sns.stripplot(y='Total',x='Payment',data=mart,jitter=0.3)
# sns.violinplot(y='Total',x='Payment',data=mart,color='gray')
# plt.show()
############

sns.stripplot(y='Total',x='Payment',data=mart,jitter=0.3)
sns.boxplot(y='Total',x='Payment',data=mart,color='gray')
plt.show()




