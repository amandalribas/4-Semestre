
#x = solução exata, x0 = solução aproximada
def erro(x,x0):
    return x - x0

def erro_abs(x,x0):
    return abs(erro(x,x0))

def erro_rel(x,x0):
    return erro_abs(x,x0)/abs(x)

def printa_erro(x):
    for i in range(len(x)):
        print(f"i = {i}; {x[i]}")


def printa_desvio(x):
    for i in range(1,len(x)):
        print(f"i = {i}; {x[i]}")



xi = [2,1.5,1.4166666666666665, 1.4142156862745097,1.4142135623746899]

#DESVIO i = 1 a i=4
d_abs = [0]*5
d_rel = [0]*5
for i in range (1,len(xi)):
    d_abs[i] = erro_abs(xi[i],xi[i-1])
    d_rel[i] = erro_rel(xi[i],xi[i-1])

print("a)DESVIOS ABSOLUTOS:")
printa_desvio(d_abs)

print("\nb)DESVIOS RELATIVOS")
printa_desvio(d_rel)

x = 2**(1/2)

e_abs = [0]*5
e_rel = [0]*5

for i in range (len(xi)):
    e_abs[i] = erro_abs(x,xi[i])
    e_rel[i] = erro_rel(x,xi[i])


print("\nc)ERROS ABSOLUTOS:")
printa_erro(e_abs)

print("\nd)ERROS RELATIVOS:")
printa_erro(e_rel)