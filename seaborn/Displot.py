import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

mart=pd.read_excel('supermarket_sales.xlsx')
mart=mart[['Gender','Payment','Unit price','Quantity','Total','gross income','Branch']]
mart.head()

# sns.displot(data=mart,x='Total',kde=True,rug=True,rug_kws={'height':0.05},kde_kws={'bw_adjust':7}
#             ,hue='Payment',multiple='stack',col='Branch',row='Gender')
# plt.show()
###########

sns.displot(data=mart,x='Total',kind='ecdf',hue='Payment',col='Branch',row='Gender')
plt.show() 
























