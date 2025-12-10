import pandas as pd

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,4],'C':[21,22,23,24]})
# print(pd.merge(var1,var2,on='A'))

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})      #only same elements in a
# var2 = pd.DataFrame({'A':[1,2,3,5],'C':[21,22,23,24]})
# print(pd.merge(var1,var2))

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})      #only same elements in a
# var2 = pd.DataFrame({'A':[1,2,3,5],'C':[21,22,23,24]})
# print(pd.merge(var1,var2,how = 'left'))                     #how = left,inner,right,outer

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,5],'C':[21,22,23,24]})
# print(pd.merge(var1,var2,how = 'outer',indicator=True))

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})
# print(pd.merge(var1,var2,left_index=True,right_index=True,suffixes=('name','python')))

                    #   CONCAT

# sr1 = pd.Series([1,2,3,4])
# sr2 = pd.Series([11,12,13,14])
# print(pd.concat([sr1,sr2]))

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})
# print(pd.concat([var1,var2],axis=1))

# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})
# print(pd.concat([var1,var2],axis=0,keys=['d1','d2']))
#
# var1 = pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]})
# var2 = pd.DataFrame({'A':[1,2,3,5],'B':[21,22,23,24]})
# print(pd.concat([var1,var2],axis=0,join='inner',keys=['d1','d2']))

                # GROUPBY
# var = pd.DataFrame({'name':['a','b','c','d','a','b','a','b','a','c','c','d'],
#                               's1':[12,13,14,15,13,17,18,19,10,29,39,13],
#                               's2':[72,83,74,95,33,27,18,99,80,79,39,53]})
# print(var)
# var_new = var.groupby('name')                           # it brings all a,b,c together
# print(var_new)
# for x,y in var_new:
#     print(x)
#     print(y)
# print()
# print()
# print(var_new.get_group('a'))
# print(var_new.get_group('b'))
# print(var_new.get_group('c'))
# print()
# print(var_new.min())
# print(var_new.mean())
#
#
# li = list(var_new)
# print(li)

                                # JOIN AND APPEND

# var1= pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]},index=['a','b','c','d'])
# var2= pd.DataFrame({'C':[19,29,39,49],'D':[18,17,16,15]})
# print(var1.join(var2))


# var1= pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]},index=['a','b','c','d'])
# var2= pd.DataFrame({'C':[19,29],'D':[18,17]},index=['a','b'])
# print(var2.join(var1,how = 'outer'))                                                # how  = puter,inner,left,right

# var1= pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]},index=['a','b','c','d'])
# var2= pd.DataFrame({'C':[19,29],'B':[18,17]},index=['a','b'])
# print(var2.join(var1,how = 'outer',lsuffix='_12',rsuffix='_123'))


# var1= pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]},index=['a','b','c','d'])
# var2= pd.DataFrame({'C':[19,29],'B':[18,17]},index=['a','b'])
# print(var1._append(var2))

# var1= pd.DataFrame({'A':[1,2,3,4],'B':[11,12,13,14]},index=['a','b','c','d'])
# var2= pd.DataFrame({'C':[19,29],'B':[18,17]},index=['a','b'])
# print(var1._append(var2,ignore_index=True))


                                        #    MELT  AND PIVOT TABLE
# var = pd.DataFrame({'days':[1,2,3,4,5],'eng':[10,20,30,40,50],'math':[11,12,13,14,15]})
# print(pd.melt(var,id_vars=["days"],var_name = 'python',value_name='wscubbe'))

var = pd.DataFrame({'days':[1,2,3,4,5],'st_name':['a','b','a','c','b'],'eng':[10,20,30,40,50],'math':[11,12,13,14,15]})
print(var)
print(var.pivot(index='days',columns='st_name'))
print()
print(var.pivot(index='days',columns='st_name',values="eng"))
print()
print(var.pivot_table(index='st_name',columns='days',aggfunc='mean',margins=True))