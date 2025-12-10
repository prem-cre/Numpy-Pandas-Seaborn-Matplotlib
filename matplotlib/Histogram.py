import matplotlib.pyplot as plt
import numpy as np
import random
# no=np.random.randint(10,20,(50))        # generated random no for plotting random no
# print(no)
# l=[10,20,30,40,50,60]                                               #orientation=horizontal,vertical
# plt.hist(no,'auto',(0,100),edgecolor="r",align='left')         #cumlatve reverses the graph
# plt.title('random no')                                                  #bottom=20 strts y from 20
# plt.xlabel('rad .no')                                               #histtype=bar,barstackeed,step,stepfilled
# plt.ylabel('percentage')
# plt.axvline(45,color='g',label='line')
# plt.legend()
# plt.grid()
# plt.show()

# x=[10,20,30,40]
# x1=[40,30,20,10]
# y=['c','c++','java','python']
# ex=[0.4,0.0,0.0,0.0]
# plt.pie(x,labels=y,radius=1)
# plt.pie(x1,radius=0.5)
#
# plt.show()

                        # donut piechart

x=[10,20,30,40]
x1=[40,30,20,10]
y=['c','c++','java','python']

plt.pie(x,labels=y,radius=1.5)
cr=plt.Circle(xy=(0,0),radius=1,facecolor='w')
plt.gca().add_artist(cr)

plt.show()


