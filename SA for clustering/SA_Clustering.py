# Simulated Annealing for Clustering Problems
import math
import random
num_objects = 10 # numbers of objects to be clustered
num_cost_increases = 100
avg_cost_increase = 200
acc_ratio = 0.75 # acceptance ratio should e between 0 and 1
prob_e = 0.00000000001 # probability factor
beta = 0.125
max_iter =  4 * num_objects # maximum number of iterations
num_temp = 200
k = 6 # number of labels
# SA accepts cost increse beta * avg_cost_increase at the probability of prob_e

initial_temperature = avg_cost_increase / math.log( num_cost_increases / ((num_cost_increases * acc_ratio) - (1-acc_ratio) * (max_iter - num_cost_increases)))
final_temperature = -beta * avg_cost_increase / math.log(prob_e)
alpha = math.pow(final_temperature / initial_temperature , 1 / num_temp) # decay rate for temperature

initial_state = {1:'A', 2: 'B', 3:'A', 4:'B', 5:'C', 6:'B', 7:'A', 8:'None', 9:'None', 10:'None' }
unused_labels = ['D', 'E', 'F']

def Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state, unused_labels):
    t = initial_temperature
    current_state = initial_state.copy()
    print("Original State:", current_state)
    print("Energy of Original State:", value(current_state))
    while(t >= final_temperature):
        for i in range(1, max_iter):
            next_state = action_on(current_state)
            energy_delta = value(next_state) - value(current_state)
            if ((energy_delta < 0) or (math.exp( -energy_delta / t) >= random.randint(0,10))):
                current_state = next_state
        t = alpha * t
    print("Final", current_state)
    print("Energy of final state:", value(current_state))

def action_on(p):
    curr = p.copy()
    n = num_objects
    l=[] # list of used labels
    for j in range(1,len(p)):
        if ((p[j] not in l)):
            l.append(p[j])
    lc = unused_labels.copy() # list of unused labels
    perturbed_state = p.copy() # state upon which the action is done
    i = random.randint(1,n) # choose a random object
    while (True):
        m = random.randint(0, len(l)) # index of the random object
        if len(l) == k or m>0:
            index1 = random.randint(0,len(l)-1)
            perturbed_state[i] = l[index1]
        else:
            try:
                index2 = random.randint(0, len(lc)) - 1
                perturbed_state[i] = lc[index2]
                lc.remove(lc[index2])
            except:
                print("ALL ARE USED")
        if(perturbed_state[i] != p[i]): # check whether the disturbed state is different from current_state
            break
    return perturbed_state # return state upon which the action is done.

def value(state):
    c=0
    for i in range(1, len(state)):
        if(state[i] == 'F'):
            c+=1
    energy = num_objects - c
    return energy # energy of the state

if __name__ == "__main__":
    Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state, unused_labels )
