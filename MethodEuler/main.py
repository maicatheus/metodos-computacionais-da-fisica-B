from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 

def main():
    eulerMethod = EulerMethod(100)
    t0=0
    tf=5
    dt=0.2
    cte=1

    t,F = eulerMethod.eulerExplicit(t0,tf,dt,cte)

    plt.title("Decaimento Radioativo")
    plt.plot(t,F,label = "Explicit")
    plt.legend()

    t,F = eulerMethod.eulerImplicit(t0,tf,dt,cte)
    plt.plot(t,F, label = "Implicit")
    plt.legend()


    plt.show()

main()


    

