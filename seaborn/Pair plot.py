import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')

# sns.pairplot(data=mart)
# plt.show()
#########

# sns.pairplot(data=mart,diag_kind='kde')           #changing diagonal plots
# plt.show()
########

# sns.pairplot(data=mart,kind='reg')                                 # changing rest plots
# plt.show()
############

# sns.pairplot(data=mart,hue='Gender')
# plt.show()
######

# sns.pairplot(data=mart,x_vars=['Rating','Payment'],y_vars=['Total'])
# plt.show()
##########

# sns.pairplot(data=mart,corner=True)
# plt.show()
#########

# sns.pairplot(data=mart,plot_kws=dict(color='r',marker=10,s=100))
# plt.show()
############

# l=sns.pairplot(data=mart)
# l.map_upper(sns.kdeplot)
# plt.show()






