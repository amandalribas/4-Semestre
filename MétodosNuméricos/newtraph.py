import numpy as np
from matplotlib import pyplot as plt

def newtonraphson(f,fd,x0,tol=1e-06,maxit=1000):
    ii=0
    x=x0
    fx=f(x)
    delta=np.abs(fx)
    print(f'iter {ii}, x={x:.8e}, f(x)={fx:.8e}')
    while(delta>tol and ii<maxit):
        ii+=1
        x -= (fx/fd(x))
        fx=f(x)
        delta=np.abs(fx)
        print(f'iter {ii}, x={x:.8e}, f(x)={fx:.8e}')
    return x 


def newtonraphson_graphic(f,fd,x0,xlim,tol=1e-06,maxit=1000):
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(2,1)
    x = np.linspace(xlim[0],xlim[1],10001,dtype='float64')
    y = f(x)
    ax1.plot(x,y,'b-')
    ax1.plot(xlim,[0,0],'k:')  
    ii=0
    x=x0
    fx=f(x)
    delta=np.abs(fx)
    x_plt, = ax1.plot(x,fx,'g.', markersize=20)
    next_x = x-(fx/fd(x))
    tan_plt, = ax1.plot([x,next_x,next_x],[fx,0,f(next_x)],'r--')
    iter_x = np.linspace(0,maxit,maxit+1)
    res_y = np.zeros(np.shape(iter_x))
    res_y[0]=delta
    res_plt, = ax2.plot(iter_x[:ii+1],res_y[:ii+1],'b--.')
    ax2.set_xlim([-0.5,2])
    ax2.set_ylim([tol*1e-01,1e+02])
    ax2.set_yscale('log')
    print(f'iter {ii}, x={x:.8e}, f(x)={fx:.8e}')
    _=input('')
    while(delta>tol and ii<maxit):
        ii+=1
        x -= (fx/fd(x))
        fx=f(x)
        delta=np.abs(fx)
        res_y[ii]=delta
        x_plt.set_data([x],[fx])
        next_x = x-(fx/fd(x))
        tan_plt.set_data([x,next_x,next_x],[fx,0,f(next_x)])
        res_plt.set_data([iter_x[:ii+1]],[res_y[:ii+1]])
        ax2.set_xlim([-0.5,ii+1])
        if (delta<tol*1e-01):
          ax2.set_ylim([10**(np.log10(delta)-1.),1e+02])
        print(f'iter {ii}, x={x:.8e}, f(x)={fx:.8e}')
        _=input('')
    return x

if __name__ == '__main__':
    #my_f  = lambda x : -np.power(x,2.) + 4.
    #my_fd = lambda x : -2.*x
    
    #my_f  = lambda x : -np.exp(x) + 5.
    #my_fd = lambda x : -np.exp(x)
    
    my_f = lambda x : 5 - np.power(x,3)
    my_fd = lambda x : -3*np.power(x,2)

    #newtonraphson(my_f,my_fd,5.0)
    newtonraphson_graphic(my_f,my_fd,2.5,[-1.0,3.0])
    
    #my_f  = lambda x :  5. / (x+1.) + 2.*np.exp(x-3.)-4.
    #my_fd = lambda x : -5. / np.power(x+1.,2) + 2.*np.exp(x-3.)
    #newtonraphson(my_f,my_fd,2.5)
    #newtonraphson_graphic(my_f,my_fd,2.5,[-0.5,4.5])
    
    _ = input('')