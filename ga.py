...
#initial population of random bitstring
pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]

...
#enumerate generations
for gen in range(n_iter):
...

#evaluate all candidates in the population
scores = [objective(c) for c in pop]

#tournament selection
def selection(pop,scores,k=3):
    #first random selection
    selection_ix = randint(len(pop))
    for ix in randomint(0,len(pop))
    #check if better (e.g. perform a tournament)
    if scores[ix] < scores[selection_ix]:
    selection_ix = ix
    return pop[selection_ix]