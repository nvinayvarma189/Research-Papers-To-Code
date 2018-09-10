# Simulated Annealing for Clustering Problems
import math
import random
num_objects = 10 # numbers of objects to be clustered
num_cost_increases = 100
avg_cost_increase = 200
acc_ratio = 0.75 # acceptance ratio should e between 0 and 1
prob_e = 0.00000000001
beta = 0.125
max_iter =  4 * num_objects
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
    while(t >= final_temperature):
        for i in range(1, max_iter):
            next_state = action_on(current_state)
            # print()
            # print("next_state", next_state)
            # print("current_state", current_state)
            # print(value(next_state))
            # print(value(current_state))
            energy_delta = value(next_state) - value(current_state)
            # exit()
            if ((energy_delta < 0) or (math.exp( -energy_delta / t) >= random.randint(0,10))):
                current_state = next_state
        t = alpha * t
    print("Final", current_state)

def action_on(p):
    curr = p.copy()
    n = num_objects
    l=[]
    for j in range(1,len(p)):
        if ((p[j] not in l)):
            l.append(p[j])
    lc = unused_labels.copy()
    perturbed_state = p.copy()
    # print()
    # print("original", curr)
    i = random.randint(1,n)
    while (True):
        m = random.randint(0, len(l))
        # print("index of dstate:",i,"list of used labels:", l, "M:", m)
        if len(l) == k or m>0:
            index1 = random.randint(0,len(l)-1)
            # print("index of labels", index1)
            perturbed_state[i] = l[index1]
            # print("disturbed state", perturbed_state)
        else:
            try:
                index2 = random.randint(0, len(lc)) - 1
                # print()
                # print(lc)
                # print("index_2", index2)
                perturbed_state[i] = lc[index2]
                # print()
                # print("unused dstate:", perturbed_state)
                lc.remove(lc[index2])
                # l.append(lc[index2])
            except:
                print("ALL ARE USED")
        if(perturbed_state[i] != p[i]):
            break
    return perturbed_state

def value(state):
    c=0
    for i in range(1, len(state)):
        if(state[i] == 'D'):
            c+=1
    energy = num_objects - c
    return energy

if __name__ == "__main__":
    Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state, unused_labels )
