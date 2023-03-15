import random

#initializtion of weight and value
best=-50000
W=[5,3,7,2]
V=[12,5,10,7]
Knapsack_Value=12

#initializtion of population
populations=([[random.randint(0,1) for x in range(4)] for y in range(4)])
# print(type(populations))
print("First generation popultions\n",populations)

#Fitness Score Calculation 
def fitness_score() :
    global populations,best
    fit_value =[0,0,0,0]
    weight_value=[0,0,0,0]
    # fit_score=[]
    for i in range(4) :
        for j in range(4):
            if(populations[i][j]==1):
                fit_value[i]+=V[j]
                weight_value[i]+=W[j]
        if(weight_value[i]>Knapsack_Value):
            fit_value[i]=0
            
    print("fitness value\n",fit_value)
    print("Weight value\n",weight_value)
    fit_value, populations = zip(*sorted(zip(fit_value, populations) , reverse = True))
    print("P",populations)
    best=fit_value[0]
    
#selection parent
def selectionParent():
    global parents
    parents=populations[0:2]
    # print(type(parents))
    print("selected Parent\n",parents)
    
#new gneration with crossover
def crossover():
    global parents
    crossover_point= random.randint(0,2)
    print("Crossover_point :",crossover_point+1)
    parents=parents+tuple([(parents[0][0:crossover_point+1]+parents[1][crossover_point+1:4])])
    parents=parents+tuple([(parents[1][0:crossover_point+1]+parents[0][crossover_point+1:4])])
    print("After Crossover\n",parents)
    
#new generation with mutation
def mutation():
    global populations,parents,x,y
    if parents[0][1]==1:
        x=random.randint(0,3)
        y=random.randint(0,3)
        parents[x][y]=1-parents[x][y]
    populations=parents
    print("After Mutation\n",populations[2:4])

for i in range(1000):
    fitness_score()  
    selectionParent()
    crossover()
    mutation()
    
print("Best score:",best)
print("Gene Sequence:\n",populations[0])



