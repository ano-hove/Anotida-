#1.infect
import random 
def infect(infection_prob: float) -> bool:
    """This function takes a float giving the infection
       probability for the disease, and randomlyreturns
       True or False, indicating if an infection has occurred."""
    
    #Generate random floating number between 0 and 1 
    random_value = random.uniform(0,1)
    
    #Compare generated number with probability, if less return true
    return random_value < infection_prob


#Test code
total_infected = 0
total_uninfected = 0
for trial in range(1000):
    result = infect(.2)
    if result == True:
            total_infected += 1
    else:
        total_uninfected += 1
print(result)

#2.recover
def recover(recovery_prob: float) -> bool:
    """This function takes a float giving the recovery
       #probability for a person infected with the disease,
       #and randomly returns True or False, indicating if the person
       #has recovered (True means they recover."""
    
    #Generate a random number between 0 an 1 
    random_value = random.uniform(0,1)
    
    #Compare the generated number with recovery probability
    return random_value < recovery_prob



#test code
total_recovered = 0
total_not_recovered = 0

for trial in range(1000):  
    result = recover(0.5)  
    if result == True:  
        total_recovered += 1
    else:  
        total_not_recovered += 1
print(result)




#3.contact indices
def contact_indices(pop_size: int, source: int, contact_range: int)->list:
    """This function determines which people come into contact with an
       infected person, and returns the list of indices of these
       people."""
    #determine the start and stop for the range
    start = max(0, source - contact_range)
    end = min(pop_size, source + contact_range + 1)

    #Generate the list of indices
    result = []
    for i in range(start, end):
        if i != source:
            result.append(i)
    return result

# test code
pop_size = 10
source = 5
contact_range = 2
print(contact_indices(pop_size, source, contact_range))



#4.Apply recoveries

def apply_recoveries(population: list, recovery_prob: float)->list:
    """This function takes the list of strings (population)
       giving the status of the population, and the recovery
       probability for the disease (described in the description
       of recover)."""

    #Iterate through list
    for i in range(len(population)):
        #check if person is infected
        if population[i] == 'I':
            #use recovery function to determine if they recover
            if recover(recovery_prob):
                population[i] = 'R'

    return list

#test code
population = ['S', 'I', 'S', 'I', 'R', 'I']
# 50% chance of recovery
recovery_prob = 0.5  
# Call the apply_recoveries function
apply_recoveries(population, recovery_prob)
# Print the updated population after applying recoveries
print(population)


#5.Contact
def contact(population:list, source:int, contact_range:int, infect_chance:float)->list:
    """This function simulates an infected person coming into contact with other
       people, possibly infected them. It takes four arguments: the list of strings
       giving the status of the population (population); the index of the infected
       person (source); an integer giving the contact range (contact range), described
       in the instructions for contact indices; and the infection probability of the
       disease (infect chance)."""

    #get list of indices that the inefected person contacts
    contact_indices_list = contact_indices(len(population), source, contact_range)

    #iterate through the people the infected person comes into contact with
    for index in contact_indices_list:
        if population[index] == 'S':
            if infect(infect_chance):
                population[index] = 'I'

    return list
# Example population: S = susceptible, I = infected, R = recovered
population = ['S', 'I', 'S', 'S', 'S', 'I', 'S', 'S']
# Infected person at index 1
source = 1
# Infected person can contact up to 2 people before and after them
contact_range = 2
# 30% chance of infecting a susceptible person
infect_chance = 0.3  
# Call the contact function
contact(population, source, contact_range, infect_chance)
# Print the updated population after contact and possible infections
print(population)

#6.applycontacts
def apply_contacts(population:list, contact_range:int, infect_chance:float)-> None:

    """This function simulates all of the infected people in the population
       coming into contact with other people, possibly infecting them. It takes three
       arguments: the list of strings giving the status of the population
       (population);an integer giving the contact range (contact range),
       described in the instructions for contact indices; and the infection
       probability of the disease (infect chance)."""

    
    #create an empty list to store indices
    infected_indices = []
    #identify infected poeple
    for index in range(len(population)):
        if population[index]== 'I':
            infected_indices.append(index)
    #contacts  for each infected person
    for source in infected_indices:
        #use contact function to simulate interactions.
        contact(population, source,contact_range, infect_chance)
        
    return None


#Test code
population = ['S', 'I', 'S', 'I', 'S', 'S']
contact_range = 1
infect_chance = 0.5

apply_contacts(population, contact_range, infect_chance)
print("After apply_contacts:", population)


             
#7.population_SIR_counts
def population_SIR_counts(population:list)->dict:
    """This function takes a list of strings giving the status of
       the population (population). It counts the number of people who
       are susceptible, infected, and recovered, and returns these
       counts in a dictionary, where the keys are the strings
       ‘susceptible’, ‘infected’, and ‘recovered’."""
    #Initialize counters
    counts = {'susceptible': 0, 'infected': 0, 'recovered': 0}

    #Count each type of status
    for status in population:
        if status == 'S':
            counts['susceptible'] += 1
        elif status == 'I':
            counts['infected'] += 1
        elif status == 'R':
            counts['recovered'] += 1

    return counts

# test code 
population = ['S', 'I', 'S', 'R', 'S', 'I', 'R', 'R', 'S']

# Call the function and print the result
sir_counts = population_SIR_counts(population)
print(sir_counts)



#8.Simulate day

def simulate_day(population: list, contact_range: int, infect_chance:float, recover_chance:float)-> None:
    """This function simulates one day in the progression of the disease. It
       takes four arguments: the list of strings giving the status of the
       population (population); an integer giving the contact range
       (contact range); the infection probability of the disease
       (infect chance); and the recovery probability for a person infected
       with the disease (recover chance)."""

    #simulate recoveries
    apply_recoveries(population, recover_chance)

    #simulate contacts and possible infections
    apply_contacts(population, contact_range, infect_chance)

    return None

#test code
population = ['S', 'I', 'S', 'I', 'S', 'R']
contact_range = 1
infect_chance = 0.5
recover_chance = 0.3


simulate_day(population, contact_range, infect_chance, recover_chance)
print("After simulation:", population)


#Note: you will not be able to call these functions until you have implemented the other functions for this project.

def initialize_population(pop_size:int) -> list:
    population = ['S'] * pop_size
    population[0] = 'I'
    return population

def simulate_disease(pop_size:int, contact_range:int, infect_chance:float, recover_chance:float) -> list:
    population = initialize_population(pop_size)
    counts = population_SIR_counts(population)
    all_counts = [counts]
    while counts['infected'] > 0:
        simulate_day(population, contact_range, infect_chance, recover_chance)
        counts = population_SIR_counts(population)
        all_counts.append(counts)
    return all_counts

def peak_infections(all_counts:list) -> int:
    max_infections = 0
    for day in all_counts:
        if day['infected'] > max_infections:
            max_infections = day['infected']
    return max_infections
        
def display_results(all_counts:list) -> None:
    num_days = len(all_counts)
    print("Day".rjust(12) + "Susceptible".rjust(12) + "Infected".rjust(12) + "Recovered".rjust(12))
    for day in range(num_days):
        line = str(day).rjust(12)
        line += str(all_counts[day]["susceptible"]).rjust(12)
        line += str(all_counts[day]["infected"]).rjust(12)
        line += str(all_counts[day]["recovered"]).rjust(12)
        print(line)
    print("\nPeak Infections: {}".format(peak_infections(all_counts)))

    
counts = simulate_disease(100, 2, .2, .05)
display_results(counts)

