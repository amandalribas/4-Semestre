import numpy as np


#P = {(3.7, 10.0), (7.9, 20.8), (5.8, 16.6), (8.9, 24.0), (4.2, 12.0),(5.3, 15.6)},
x = np.array([3.7,7.9,5.8,8.9,4.2,5.3], dtype='float32')
y = np.array([10,20.8,16.6,24,12,15.6], dtype='float32')

############letra a) Encontrando a0 e a1
a1 = lambda x, y, n = len(x): (n * (sum(x * y)) - (sum(x) * sum(y)))/(n * sum(x**2) - sum(x)**2)
a1 = a1(x,y)

a0 = lambda x, y, a1, n = len(x): 1/n *(sum(y) - sum(x)*a1)
a0 = a0(x,y,a1)

print(f"f(x)= {a0:.4f} + {a1:.4f}x")

print()

#letra b) Encontrando r**2
y_medio = sum(y)/len(y)

E_medio = sum((y-y_medio)**2)
E = sum((y - a0 - a1*x)**2)
r2 = abs(E-E_medio)/E_medio
print(f'r2 = {r2}, se r2>=0.95 bom!')

#letra c) f(3) e f(6)
print()
f = lambda x, a0=a0, a1=a1: a0 + a1*x
print(f"f(3)= {f(3)}")
print(f"f(6)= {f(6)}")