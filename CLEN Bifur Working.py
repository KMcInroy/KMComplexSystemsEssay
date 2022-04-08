import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
aarr=np.arange(0,2,0.01)
rarr=np.arange(1,4,0.01)
Ls=np.empty(0)
BifurPlot=np.empty(0)
sigma=0.1
for r in rarr:
#for a in aarr:
    x = 0.1
    ls = np.empty(0)
    for t in range(100):
       # x = (1 - a*x**2)+np.random.normal(0,sigma,1)
        x=r*x*(1-x)+np.random.normal(0,sigma,1)
    # ignoring first 100 iterations
    for t in range(200):
        #x = (1 - a*x**2)+np.random.normal(0,sigma,1)
        x=r*x*(1-x)+np.random.normal(0,sigma,1) 
        BifurPlot=np.append(BifurPlot,x)
        #ls=np.append(ls,abs(2*a*x))
        ls=np.append(ls,abs(r-2*r*x))
    Ls=np.append(Ls,np.mean(np.log(ls)))

print(max(Ls[Ls < 1E308]))
RAxis=np.linspace(1,4,len(BifurPlot))
#plt.plot(RAxis[RAxis>3],BifurPlot[len(RAxis[RAxis<3]):],'.',markersize=1)
plt.plot(RAxis,BifurPlot,'.',markersize=1)
plt.ylim(-1*0.1 , 1.1)
plt.ylabel("Possible $x_{t}$")
plt.xlabel("r")
plt.show()
#plt.plot(aarr,Ls)
#plt.plot(aarr,np,zeros(len(aarr)))
plt.plot(rarr,Ls,label="Lyapunov exponenet behaviour")
plt.plot(rarr,np.zeros(len(rarr)),label="Threshold for Chaos")
plt.ylim(-4,1)
plt.xlabel("r")
plt.ylabel("$\lambda$")
#plt.legend(loc="best")
plt.show()
xG=np.linspace(-1*5,5,10000)
G=stats.norm.pdf(xG, 0, 1)

plt.plot(xG,G)
plt.xlabel("$\epsilon$")
plt.ylabel('$P_{\epsilon}$')
#0.660187399058728
#0.6522426054667301
#0.6420591990894897
#0.6465415889877147
#0.658332563212218
#0.6536891093033291