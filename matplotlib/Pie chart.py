import matplotlib.pyplot as plt
# x=[10,20,30,40]
# y=['c','c++','java','python']
# ex=[0.4,0.0,0.0,0.0]
# plt.pie(x,labels=y,explode=ex,autopct='%0.1f%%',shadow=True,radius=1.5,labeldistance=1.1,startangle=90
#         ,textprops={'fontsize':18.5},counterclock=False,wedgeprops={'linewidth':8})        #0.1 is decimal point
#
# plt.legend(loc=1)             # loc =1,2,3,4
# plt.show()


# x=[10,20,30,40]
# x1=[40,30,20,10]
# y=['c','c++','java','python']
# ex=[0.4,0.0,0.0,0.0]
# plt.pie(x,labels=y,radius=1)
# plt.pie(x1,radius=0.5)
#
# plt.show()


x=[10,20,30,40]
x1=[40,30,20,10]
y=['c','c++','java','python']

plt.pie(x,labels=y,radius=1.5)
plt.pie(x1,radius=0.5)

plt.show()







