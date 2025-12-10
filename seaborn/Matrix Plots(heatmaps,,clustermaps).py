import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')
#
# pt=sns.FacetGrid(mart,col='City')
# pt.map_dataframe(sns.kdeplot,x='Rating',hue='Gender')
# plt.show()
#############

pt=sns.FacetGrid(mart,col='City',row='Payment',sharey=False,ylim=(0,100))
pt.map_dataframe(sns.histplot,x='gross income')
pt.set_axis_labels('gross income','Total')
pt.set_titles(col_template='{col_name} ',row_template='{row_name}')
plt.show()















