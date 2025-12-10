import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.histplot(x='Total',data=mart,binwidth=150,bins=np.arange(0,1100,50))
# plt.show()
#########

# plt.figure(figsize=(15,5))
# sns.histplot(x='Total',data=mart,binwidth=150,bins=np.arange(0,1100,50))
# plt.xticks(np.arange(0,1100,50))
# plt.show()
########

# sns.histplot(x='Total',data=mart,kde=True,hue='Payment',multiple='stack')
# plt.show()
#######

# sns.histplot(x='Total',data=mart,element='poly',fill=True,hue='Payment',)
# plt.show()                                        #element = poly ,step
########
#
# sns.histplot(x='Total',data=mart,stat='probability')        #stat=count,density,probability,frequency
# plt.show()                                      #shrink makes this as a bar plot


sns.histplot(x='Total',data=mart,y='gross income')
plt.show()