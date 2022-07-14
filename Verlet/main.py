from Methods import Methods
import matplotlib.pyplot as plt 
def main():
    initial_x = 3
    initial_v = 0
    k = 1
    m = 10
    t0 = 0
    tf = 50
    dt = 0.05
    #dt = 0.05*(2*math.pi*math.sqrt(m/k))
    

    verlet  = Methods(initial_x,initial_v,k,m,t0,tf,dt)
    period, vel_list, x_list,E_list = verlet.Verlet()

    plt.figure(1)
    plt.xlabel("Position")
    plt.ylabel("Velocity ")
    plt.title("Phase portrait")
    plt.plot(x_list,vel_list,label = f"dt = {dt}")
    plt.legend()
    
    plt.figure(2)
    plt.xlabel("time")
    plt.ylabel("position")
    plt.title("Spring Verlet")
    plt.plot(period,x_list,label = f"dt = {dt}")
    plt.legend()

    plt.figure(3)
    plt.xlabel("time")
    plt.ylabel("Energy")
    plt.title("Total energy")
    plt.plot(period,E_list,label = f"dt = {dt}")
    plt.legend()


    plt.show()


    
main()