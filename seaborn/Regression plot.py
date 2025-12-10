import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx').sample(50)

sns.regplot(data=mart,x='Rating',y='Total',line_kws=dict(color='red',linestyle='--'),scatter_kws=dict(color='g',s=100))
plt.show()


















