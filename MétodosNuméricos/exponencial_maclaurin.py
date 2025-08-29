import numpy as np
from matplotlib import pyplot as plt

plt.ion() #nao precisa chamar o plt.show() toda vez
fig, (ax1, ax2) = plt.subplots(2,1)

##############

dx = 1.0 #distancia aproximada entre cada ponto
xmax = 5.0
xmin = -5.0

n = int((xmax - xmin)/dx)
x = np.linspace(xmin, xmax, n,dtype='float32')
print(x)
y = np.exp(x,dtype='float32')
ax1.plot(x,y,'b.')
_=input(" ")

dx = 2.0
n = int((xmax-xmin)/dx)
x = np.linspace(xmin, xmax, n,dtype='float32')
print(x)
y = np.exp(x,dtype='float32')
ax1.plot(x,y,'r+')

_=input(" ")

############

dx = 0.05
n = int((xmax-xmin)/dx)
x = np.linspace(xmin,xmax,n,dtype='float32')
print(x)
y = np.zeros(x.shape,dtype='float32')
err = np.zeros(x.shape,dtype='float32')
y_exp = np.exp(x,dtype='float32')
factorial = 1
for ii in range(10):
    y[:] += np.power(x,ii) * (1/factorial)
    err[:] = np.abs(y_exp - y) #valor exato - aproximacao
    ax1.plot(x,y)
    ax2.plot(x,err)
    factorial *= ii + 1
    print(ii)
    _=input(" ")
