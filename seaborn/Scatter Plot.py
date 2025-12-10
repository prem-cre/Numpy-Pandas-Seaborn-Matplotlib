import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx').sample(50)
mart.head()

# sns.scatterplot(data=mart,x='Product line',y='Total',hue='Gender')
# plt.show()
#########

# sns.scatterplot(data=mart,x='Product line',y='Total',style='Gender')                          #markers={'Male':'^','Female':'o'}
# plt.show()
#######

# sns.scatterplot(data=mart,x='Product line',y='Total',style='Gender',markers={'Male':'^','Female':'o'},hue='Payment')
# plt.show()
#########

sns.scatterplot(data=mart,x='Product line',y='Total',size='Gender',sizes=(20,200),legend='full',markers={'Male':'^','Female':'o'},hue='Payment')
plt.show()








