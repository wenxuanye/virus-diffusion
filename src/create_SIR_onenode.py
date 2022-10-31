# for each node, we build an isolated cases
# the initial state is (N0-I0,I0,0,N0,β,γ)
# S0 is the initial number of susceptible individuals
# I0 is the initial number of infected individuals
# R0 is the initial number of recovered individuals
# N0 is the total population
# β is the infection rate
# γ is the recovery rate
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def create_SIR_eachnode(G):
    dataframe = pd.DataFrame({'S':[],'I':[],'R':[],'N':[],'β':[],'γ':[]})
    for node in G:
        N0 = np.random.randint(100,1000)
        I0 = np.random.randint(1,10)
        S0 = N0 - I0
        R0 = 0
        β = np.random.normal(1,0.1)
        γ = np.random.normal(1,0.1)
        dataframe = pd.concat([dataframe, pd.DataFrame({'S':[S0],'I':[I0],'R':[R0],'N':[N0],'β':[β],'γ':[γ],'loc':[node],'time':[0]})], ignore_index=True)
        for time in range(1,4):
            S0 = S0 - β*S0*I0/N0
            I0 = I0 + β*S0*I0/N0 - γ*I0
            R0 = R0 + γ*I0
            S0 = int(S0)
            I0 = int(I0)
            R0 = int(R0)
            dataframe = pd.concat([dataframe,pd.DataFrame({'S':[S0],'I':[I0],'R':[R0],'N':[N0],'β':[β],'γ':[γ],'loc':[node],'time':[time]})],ignore_index=True)
    return dataframe


