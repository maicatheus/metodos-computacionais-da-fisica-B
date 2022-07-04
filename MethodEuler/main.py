from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 

def main():
    initial_condition = 10
    t0=0
    tf=1E3
    steps = 1E4
    cte=0.1
    K = 1E4
    dt = 0.1

    eulerMethod = EulerMethod(initial_condition,t0,tf,dt)
    
    t_exp,F_exp = eulerMethod.eulerExplicit(cte,K,steps)
    
    t_anal, F_anal = eulerMethod.eulerAnalytic(cte,K,steps)

    plt.figure(1)
    plt.title("Populaiton growth")
    plt.plot(t_exp,F_exp,label = f"Explicit dt={dt}")
    plt.legend()

    plt.plot(t_anal,F_anal,label = f"Analytic dt={dt}")
    plt.legend()
       
    
    
    error_list = list()
    dt_list = list()
    for index in range(1,11):
        dt_list.append(dt)
    
        eulerMethod = EulerMethod(initial_condition,t0,tf,dt)
        
        t_exp,F_exp = eulerMethod.eulerExplicit(cte,K,steps)
        t_anal, F_anal = eulerMethod.eulerAnalytic(cte,K,steps)
        err = EulerMethod.Error(F_exp,F_anal,K)
        error_list.append(max(err))
        
        dt = dt*2

    
    plt.figure(2)
    plt.title("Error")
    plt.plot(dt_list,error_list,label = f"Error")
    plt.legend()

    plt.show()

main()