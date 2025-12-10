import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# aera1=[2,3,4,6,8]
# aera2=[2,3,7,6,10]
# aera3=[12,3,4,6,18]
#
# l=['area1','area2','area3']
# plt.stackplot(x,aera1,aera2,aera1,labels=l,baseline='zero')         #baseline=zero,sym,wiggle
# plt.legend()
# plt.show()


                            # STEP PLOT

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.step(x,y,label='pyhon',marker='o',ms=10,mfc='g')
plt.legend()
plt.grid()
plt.show()















