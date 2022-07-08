from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 

def main():
   
    S0=99
    I0=1
    R0=0
    gamma=0.2
    beta=0.05
    t0=0
    tf=10
    dt=0.002

    eulerMethod = EulerMethod(S0,I0,R0,gamma,beta,t0,tf,dt)
    period, S_list,I_list,R_list = eulerMethod.eulerExplicit()

    plt.figure(1)
    plt.title("SIR")
    plt.plot(period,S_list,label = f"S dt={dt}" , color = 'b')
    plt.legend()
    plt.plot(period,I_list,label = f"I dt={dt}" , color = 'r')
    plt.legend()
    plt.plot(period,R_list,label = f"R dt={dt}", color = 'g')
    plt.legend()
    plt.show()

main()