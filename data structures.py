import  pandas as pd
# x = [1,2,3,4,6,7]
# var = pd.Series(x)
# print(var)


# x = [1,2,3,4,6,7]
# var = pd.Series(x,index=['a','s','d','f','h','t'],dtype='float',name='python')
# print(var)

# dic = {'name':['python','java','matlab'],'rank': [1,2,3]}
# var1 = pd.Series(dic)
# print(var1)

# s = pd.Series(12,index=[1,2,3,4,5,6,7])
# print(s)
# print(type(s))

# s1 = pd.Series(12,index=[1,2,3,4,5,6,7])        #in numpy it shows an error and this it shows NaN
# s2 = s = pd.Series(12,index=[1,2,3])
# print(s1+s2)

# l = [1,2,3,4,5,6]
# var = pd.DataFrame(l)
# print(type(var))
# print(var)

# d = {'a': [1,2,3,4,5],'b':[1,2,3,4,5],'d':[6,7,8,9,0]}
# var1 = pd.DataFrame(d,columns=['a','d'])  #specified columns shows them only
# print(var1)

var  = pd.DataFrame({'A':[1,2,3,4],'B':[6,7,8,9]})
# print(var)


var['C'] = var['A'] + var['B']
# print(var)

var['ptyhon'] = var['A']<=3
print(var)










