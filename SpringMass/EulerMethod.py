class EulerMethod():
    def __init__(self,initial_x,initial_v,k,m,t0,tf,dt):
        self.initial_x = initial_x
        self.initial_v = initial_v
        self.k = k
        self.m = m
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

    def acc(self,x,k,m):
        return (-(k/m)*x)

    def eulerExplicit(self):
        t = self.t0
        v = v_aux = self.initial_v
        x = self.initial_x
        period = list()
        vel_list = list()
        x_list = list()
        while (t <= self.tf):
            vel_list.append(v_aux)
            x_list.append(x)
            period.append(t)

            v = v + self.acc(x,self.k,self.m)*self.dt    
            x = x + v_aux*self.dt

            v_aux = v
            
            t += self.dt
        

        return period, vel_list, x_list

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