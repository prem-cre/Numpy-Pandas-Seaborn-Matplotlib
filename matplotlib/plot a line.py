import matplotlib.pyplot as plt
import numpy as np
# x  = ['python','java','c','c++']
# y = [2,4,6,8]
# plt.xlabel('lnaguages',fontsize = 10)
# plt.ylabel('no of pepole')
# plt.title('population')
# c = ['y','b','g','m']                                               #alpha darkens or lightens tje colour of bar
# plt.bar(x,y,width=0.7,color = c,align = 'edge',edgecolor = 'r',linewidth= 5,linestyle=":",alpha=0.4)                     #align as edge ,centre
# plt.show()


# x  = ['python','java','c','c++']
# y = [2,4,6,8]
# z=[3,4,5,6]
# plt.xlabel('lnaguages',fontsize = 10)
# plt.ylabel('no of pepole')
# plt.title('population')
# c = ['y','b','g','m']
# plt.bar(x,y,width=0.7,color = c,label='prem')                               #using label we should use legend
# plt.bar(x,z,width=0.7,color = c,label='prem')                               #using label we should use legend
# plt.legend()
# plt.show()

# TWO BARS SIDE BY SIDE

# x  = ['python','java','c','c++']
# y = [2,4,6,8]
# z=[3,4,5,6]
#
# width=0.2
# p=np.arange(len(x))
# p1=[j+width for j in p ]
#
# plt.xlabel('lnaguages',fontsize = 10)
# plt.ylabel('no of pepole')
# plt.title('population')
#
#
#
# plt.bar(p,y,width,color = 'r',label='prem')
# plt.bar(p1,z,width,color = 'y',label='prem123')                               #using label we should use legend
#
# plt.xticks(p+width/2,x,rotation=20)
# plt.legend()
# plt.show()


# x  = ['python','java','c','c++']
# y = [2,4,6,8]
# z=[3,4,5,6]
#
# width=0.2
# p=np.arange(len(x))
# p1=[j+width for j in p ]
#
# plt.xlabel('lnaguages',fontsize = 10)
# plt.ylabel('no of pepole')
# plt.title('population')
#
# plt.barh(x,y,width,color = 'r',label='prem')
# plt.barh(p1,z,width,color = 'y',label='prem123')                               #using label we should use legend
#
# plt.legend()
# plt.show()


       #        FILL BETWEEN

# import numpy as np
# x=np.array([1,2,3,4,5])
# y=np.array([1,2,3,4,5])
#
# plt.plot(x,y)
# plt.fill_between(x,y,color='g',where=(x>=2)&(x<=4),alpha=0.3)
# plt.show()


                #  CHANGE OF AXES

# x=[1,2,3,4]
# y=[3,1,5,2]
# plt.plot(x,y)
# plt.xticks(x,labels=['ython','java','c','c++'])
# plt.yticks(x)
#
# plt.xlim(0,10)
# plt.ylim(0,10)
#
# plt.axis([0,10,0,7])
# plt.show()


                    #   TEXT IN PLOTS

x=[1,2,3,4]
y=[1,2,3,4]
plt.title('python')
plt.xlabel('python123')
plt.ylabel('python123456')
# plt.text(2,5,'java',style='italic',bbox={'facecolor':'red'})
# plt.annotate('python',xy=(2,1),xytext=(3,3),arrowprops=dict(facecolor='black',shrink=100))

plt.legend(['up'],loc=9,facecolor='red',edgecolor='black',framealpha=0.5,shadow=True)

plt.plot(x,y)
plt.show()


