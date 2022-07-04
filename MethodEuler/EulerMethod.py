import math

class EulerMethod():
    def __init__(self,initialCondition,t0,tf,dt):
        self.initialCondition = initialCondition
        self.t0 = t0
        self.tf= tf
        self.dt=dt

    def eulerAnalytic(self,cte,k,steps):
        from math import exp

        initial = self.initialCondition
        
        t = self.t0
        
        c = (k - initial)/(initial*k)

        function = list()
        period = list()
        count = 0


        while(count <= steps):
            function.append(k/(1 + c*k*exp(-cte*t)))
            period.append(t)
            t += self.dt
            count += 1

        return period,function


    def derived(self,cte,N,k):
        return cte * N*(1 - N/k)
    
    def eulerExplicit(self,cte,K,steps):
        func = self.initialCondition
        t = self.t0

        period = list()
        function = list()
        count=0
        while (count <= steps):
            function.append(func)
            period.append(t)
            func = func + self.derived(cte,func,K)*self.dt
            t+=self.dt
            count+=1
        
        return period,function
    
    def eulerImplicit(self,cte,steps):
        func = self.initialCondition
        t=self.t0
        period = list()
        function = list()
        function.append(func)
        
        func_aux = self.initialCondition
        period.append(t)
        
        while (t <= self.tf):
            func = func_aux/(1 + cte*self.dt)
            func_aux = func
            function.append(func)
            t += self.dt
            period.append(t)

        return period,function       

    def Error(db1,db2,k):
        error_list = list()
        if(len(db1) == len(db2)):
            steps=(len(db1))
            for i in range(0,steps):
                err = abs(db1[i] - db2[i])/db2[i]
                error_list.append(err)

            return error_list
        else:
            print("list are not same length")