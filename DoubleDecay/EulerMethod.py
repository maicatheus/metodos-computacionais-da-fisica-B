class EulerMethod():
    def __init__(self,initialCondition_Mo,initialCondition_Tc,t0,tf,dt):
        self.initialCondition_Mo = initialCondition_Mo
        self.initialCondition_Tc = initialCondition_Tc
        self.t0 = t0
        self.tf= tf
        self.dt=dt

    def eulerAnalytic(self,cte1,cte2):
        from math import exp

        initial = self.initialCondition_Mo
        
        t = self.t0
        
        c = (cte1*initial)/(cte2 - cte1)

        function = list()
        period = list()

        while(t <= self.tf):
            function.append(c*(exp(-cte1*t) - exp(-cte2*t) ))
            period.append(t)
            t += self.dt
        return period,function

    def derived_Mo(self,cte1,n1):
        return (-cte1*n1)

    def derived_Tc(self,cte1,n1,cte2,n2):
        return (cte1*n1 - cte2*n2)

    def eulerExplicit(self,cte1,cte2,multi):
        func_Mo = self.initialCondition_Mo
        func_Tc = self.initialCondition_Tc
        t = self.t0

        period = list()
        function_Mo = list()
        function_Tc = list()
        while (t <= self.tf):
            function_Mo.append(func_Mo)
            function_Tc.append(multi*func_Tc)
            period.append(t)
            func_Mo = func_Mo + self.derived_Mo(cte1,func_Mo)*self.dt
            func_Tc = func_Tc + self.derived_Tc(cte1,func_Mo,cte2,func_Tc)*self.dt
            t+=self.dt
        
        return period,function_Mo,function_Tc
    
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