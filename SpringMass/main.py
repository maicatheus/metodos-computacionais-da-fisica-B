from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 
import math
def main():
    initial_x = 10
    initial_v = 0
    k = 1
    m = 1
    t0 = 0
    tf = 100
    dt = 0.1
    #dt = 0.05*(2*math.pi*math.sqrt(m/k))
    
    euler = EulerMethod(initial_x,initial_v,k,m,t0,tf,dt)
    
    t_exp, v_exp, x_exp = euler.eulerExplicit()
    
    plt.figure("fig 1")
    plt.xlabel("time")
    plt.ylabel("position ")
    plt.title("Spring-Mass")
    plt.plot(t_exp,x_exp,label = f"spring")
    plt.legend()
    plt.legend()
    plt.show()
    
    
main()