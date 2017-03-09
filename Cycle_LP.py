import random
n=5
maxsingle=10
maxcost=10
objective={}

def addObjective(index,value):
    objective[index]=value
    objective[2**n-index-1]=value


for i in range(2**n):
    if i not in objective:
        count=0
        if bin(i).count("1")==1:
                addObjective(i,random.randint(0,maxsingle))
        else:
            maxv=0
            for j in range(n):
                if(i&2**j==1):
                    maxv+=objective[2**j]
                addObjective(i,random.randint(0,maxv))  

    

B=objective.values()
b= [x * -1 for x in B]
C=[]
for i in range(n):
    C.append(random.uniform(0,maxcost))

a=[]
for i in range(2**n):
    temp=[]
    for j in range(n):
        num=(j+1)%n
        if((i&2**j)/2**j!=(i&2**num)/2**num):
            temp.append(1)
        else:
            temp.append(0)
    a.append(temp)
A = [ [x * -1 for x in y] for y in a]

from scipy.optimize import linprog
res = linprog(C, A_ub=A, b_ub=b,bounds=(0,None),options={"disp": True})
print res
