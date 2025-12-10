import pandas as pd
dic = {'a':[1,2,3,4],'s':[1,2,3,4],'d':[1,2,3,4]}
d =pd.DataFrame(dic)
print(d)
d.to_csv("Text_new2.csv",index=False,header=['m','n','p'])














