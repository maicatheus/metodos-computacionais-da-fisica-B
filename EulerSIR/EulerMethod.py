class EulerMethod():
    def __init__(self,S0,I0,R0,gamma,beta,t0,tf,dt):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.gamma = gamma
        self.beta = beta
        self.t0 = t0
        self.tf = tf
        self.dt = dt

    def S_derived(self,S,I):
        return -self.beta*S*I
    
    def I_derived(self,S,I):
        return self.beta*S*I - self.gamma*I

    def R_derived(self,I):
        return self.gamma*I

    def eulerExplicit(self):
        S = self.S0
        I = self.I0
        R = self.R0

        t = self.t0

        period = list()
        S_list = list()
        I_list = list()
        R_list = list()
        while (t <= self.tf):
            S = S + self.S_derived(S,I)*self.dt
            I = I + self.I_derived(S,I)*self.dt
            R = R + self.R_derived(I)*self.dt
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
            period.append(t)
            t+=self.dt
      
        return period, S_list,I_list,R_list
    

    def Error(db1,db2):
        error_list = list()
        if(len(db1) == len(db2)):
            steps=(len(db1))
            for i in range(0,steps):
                err = abs(db1[i] - db2[i])/db2[i]
                error_list.append(err)

            return error_list
        else:
            print("list are not same length")