import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns

mart=pd.read_excel('supermarket_sales.xlsx')
# plt.figure(figsize=(10,5))
# # sns.countpolt(x="Product line" ,data=mart)            #for horizontal plot y=product line
# sns.countplot(x="Product line" ,hue='Gender',data=mart,palette='gist_gray')
# plt.show()

# x= mart['Product line'].sort_values()
# print(x.unique())

#############
# plt.figure(figsize=(10,5))
# sns.countplot(x="Product line" ,data=mart,facecolor=(1,0,1,0),linewidth=5,edgecolor=sns.color_palette('dark',3))
# plt.show()



##########
# sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=["Electronic_accessories",'Fashion_accessories','Food_and_beverages','Health_and_beauty']
#                                                                     , hue_order=["Male","Female"])
# plt.show()

############
# sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=["Electronic_accessories",'Fashion_accessories','Food_and_beverages','Health_and_beauty']
#             , hue_order=["Male","Female"],capsize=0.2)
# sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=["Electronic_accessories",'Fashion_accessories','Food_and_beverages','Health_and_beauty']
#             , hue_order=["Male","Female"],ci=None,palette="cividis",saturation=5,estimator=np.median)             # estimator =np.median,sum
# plt.show()

