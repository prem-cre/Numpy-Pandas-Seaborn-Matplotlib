import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Height=[5,5,7,5,8]
age=[22,43,30,35,40]

# sns.lineplot(y=Height,x=age,estimator=None)
# plt.show()

sns.lineplot(y=Height,x=age,estimator=sum,ci='sd')
plt.show()





















