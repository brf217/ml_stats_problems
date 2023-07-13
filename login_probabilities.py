import numpy as np
import matplotlib.pyplot as plt

users = []
logins = []

filename = 'logins.csv'

#open and parse file
with open(filename) as f:
    for i in f:
        users.append(i.split(',')[0])
        logins.append(i.split(',')[1])

#create dictionary - convert to numbers while filling dictionary
from collections import defaultdict
d=defaultdict(list)
for i,j in zip(users, logins):
    d[int(i)].append(int(j))
    
#define function    
def prob(day):
    ans=[]
    for i in d.values():
        if any(j>day for j in i) and (day in i):
            ans.append(1)
        elif day in i:
            ans.append(0)
    return np.mean(ans)
        
#get probabilities for each day
d_ans={}
for i in range(0,7):
   d_ans[i] = prob(i)


#plot probs by day
fig = plt.bar(d_ans.keys(), d_ans.values())
