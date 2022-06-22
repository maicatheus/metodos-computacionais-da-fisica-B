from EulerMethod import EulerMethod
import matplotlib.pyplot as plt 

def main():
    eulerMethod = EulerMethod(100)

    t,F = eulerMethod.Calculate(0,20,0.05,1)

    plt.title("Decaimento Radioativo")
    plt.plot(t,F)
    plt.show()

main()


    

