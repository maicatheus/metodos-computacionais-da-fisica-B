from typing import Any

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
        period.append(t)

        while (t<=tf):
            func = func/(1 - self.Derived(cte,func)*dt)
            function.append(func)
            period.append(t)
            t+=dt

        return period,function