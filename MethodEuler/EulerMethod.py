from typing import Any

class EulerMethod():
    def __init__(self,initialCondition):
        self.initialCondition = initialCondition
    
    def Derived(self,cte, N):
        return -cte * N
    
    def Calculate(self,t0,tf,dt,cte):
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
