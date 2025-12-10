import matplotlib.pyplot as plt
import pylab as pl

# x=[1,2,3,4,5,6]
# y=[2,4,6,8,10,12]
# plt.stem(x,y,linefmt="ro",bottom=0,basefmt='g',label='python'
#          ,orientation='horizontal')
# plt.legend()
# plt.show()

                            #BOX AND WHISKER

x=[10,20,30,40,50,60,70,120]
# plt.boxplot(x,notch=False,vert=False,widths=0.5,tick_labels=['python'],patch_artist=True)
plt.boxplot(x,label='python',showmeans=True,whis=1.5,sym='g',boxprops=dict(color='r'))
plt.show()























