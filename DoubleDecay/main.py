from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 
import math

def main():
    initial_condition_Mo = 1
    initial_condition_Tc = 0
    halflife_Mo = 66 
    halflife_Tc = 6
    t0=0
    tf=5*halflife_Mo
    cte1= abs(math.log(2)/halflife_Mo)
    cte2= abs(math.log(2)/halflife_Tc)
    dt = 0.3

    eulerMethod = EulerMethod( initial_condition_Mo,initial_condition_Tc,t0,tf,dt)
    
    t_exp,F_Mo_exp, F_Tc_exp = eulerMethod.eulerExplicit(cte1,cte2,1)
    plt.figure("fig 1")
    plt.xlabel("time (hour)")
    plt.ylabel("number of particle")
    plt.title("Double Decay")
    plt.plot(t_exp,F_Mo_exp,label = f"Explicit Mo dt={dt}")
    plt.plot(66,0.5, 'r.' ,label = "half-life Mo")
    plt.legend()
    plt.plot(t_exp,F_Tc_exp,label = f"Explicit Tc dt={dt}")
    plt.legend()
    plt.savefig('fig1')



    

    eulerMethod = EulerMethod( initial_condition_Mo,initial_condition_Tc,t0,tf,dt)
    multi = 10
    t_exp,F_Mo_exp, F_Tc_exp = eulerMethod.eulerExplicit(cte1,cte2,multi)
    plt.figure("fig 2")
    plt.xlabel("time (hour)")
    plt.ylabel("number of particle")
    plt.title("Double Decay - 10 * Tc")
    plt.plot(t_exp,F_Mo_exp,label = f"Explicit Mo dt={dt}")
    plt.legend()
    plt.plot(t_exp,F_Tc_exp,label = f"Explicit Tc dt={dt}")
    plt.plot(22,0.72, 'r.' ,label = "max of Tc (t  ~ 22h)")
    plt.legend()
    plt.savefig('fig2')


    eulerMethod = EulerMethod( initial_condition_Mo,initial_condition_Tc,t0,tf,dt)
    plt.figure("fig 3")
    plt.xlabel("time (hour)")
    plt.ylabel("number of particle")
    plt.title("Double Decay - using variable dt")
    t_anal,F_Tc_anal = eulerMethod.eulerAnalytic(cte1,cte2)
    plt.plot(t_anal,F_Tc_anal, label = f"Analytic Tc dt={dt}")
    plt.legend()

    
    dt = [dt , dt*10]
    for dt in dt:
        eulerMethod = EulerMethod( initial_condition_Mo,initial_condition_Tc,t0,tf,dt)
        t_exp,F_Mo_exp, F_Tc_exp = eulerMethod.eulerExplicit(cte1,cte2,1)
             
        plt.plot(t_exp,F_Tc_exp, label = f"Explicit Tc dt={dt}")
        plt.legend()
    plt.savefig('fig3')

    plt.show()

main()