
cd ~/Desktop

users = []
logins = []

'''
logins in one csv column, days logged in in second, non-parsed input'''

filename = 'logins.csv'

with open(filename) as f:
    for i in f:
        users.append(i.split(',')[0])
        logins.append(i.split(',')[1])

d = {}

for i,j in zip(users, logins):
    d.setdefault(int(i), []).append(int(j))
    
    
def prob(day):
    ans=[]
    for i in d.values():
        length = len(i)
        if any(j>day for j in i):
            ans.append(1)
    return (sum(ans) / len(d.values()))
        

prob(1)

for i in range(0,8):
    print(prob(i))