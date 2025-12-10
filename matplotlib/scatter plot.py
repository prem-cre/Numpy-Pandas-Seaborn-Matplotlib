import matplotlib.pyplot as plt
# day=[1,2,3,4,5,6,7]
# no=[2,3,1,4,5,3,6]
# plt.scatter(day,no)
# plt.title('SCATTER PLOT',fontsize=20)
# plt.xlabel('students')
# plt.ylabel('students123')
# plt.show()

day=[1,2,3,4,5,6,7]
no=[2,3,1,4,5,3,6]
colors=[10,49,56,38,69,65,45]            #<--- this is colorchart or colors=['r','y','g','b','r','g','r']
sizes=[400,200,300,400,500,100,700]
plt.scatter(day,no,c=colors,s=sizes,alpha=0.4,marker='*',cmap='BrBG')
t=plt.colorbar()
t.set_label('ColorLabel')
plt.title('SCATTER PLOT',fontsize=20)
plt.xlabel('students')
plt.ylabel('students123')
plt.show()







