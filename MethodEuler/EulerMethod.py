import math

class EulerMethod():
    def __init__(self,initialCondition):
        self.initialCondition = initialCondition
    
    def Derived(self,cte, N):
        return -cte * N
    
    def eulerExplicit(self,t0,tf,dt,cte):
        func = self.initialCondition
        t=t0
        period = list()
        function = list()

        while (t<=tf):
            function.append(func)
            period.append(t)
            func = func + self.Derived(cte,func)*dt
            t+=dt
        
        return period,function
    
    def eulerImplicit(self,t0,tf,dt,cte):
        func = self.initialCondition
        t=t0
        period = list()
        function = list()
        function.append(func)

        func_aux = func + self.Derived(cte,func)*dt
        period.append(t)
        while (t<=tf):
            func = func + self.Derived(cte,func_aux)*dt
            function.append(func)
            t+=dt
            period.append(t)
            func_aux = func

        return period,function