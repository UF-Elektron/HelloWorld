# Brief:    Simulation of Lotka–Volterra equations (aka predator–prey equations)
#----------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# Growth of a rabbit population
def rabbitGrowth():
    capacity = 50  # Capacity (max Population)
    velocity = 0.5 # Rate of population growth
    steps = 30     # Simulation Steps
    
    rabbits = [0] * steps
    rabbits[0] = 2
    
    for i in range (1, steps):
        rabbits[i] = rabbits[i-1] + velocity * rabbits[i-1] * (capacity - rabbits[i-1]) / capacity
        print(rabbits[i])
        
    plt.plot(rabbits)
    plt.ylabel('Rabbit Population')
    plt.xlabel('Time')
    plt.show()

# Growth of a rabbit and Kangaroo population in competition
def rabbitKangaroo():
    rabbitCapacity = 50     # Capacity of Rabbits (max Population)
    kangarooCapacity = 10   # Capacity of Kangaroos (max Population)
    rabbitVelocity = 0.5    # Rate of population growth
    kangarooVelocity = 0.1  # Rate of population growth
    foodNeed = 5            # Difference of food needed. Kangaroos need 5 times as much as rabbits
    steps = 20              # Simulation Steps
    
    time = [x for x in range (0, steps)]
    rabbits = [0] * steps
    rabbits[0] = 2
    kangaroos = [0] * steps
    kangaroos[0] = 5
    
    for i in range (1, steps):
        rabbits[i] = rabbits[i-1] + rabbitVelocity * rabbits[i-1] * (rabbitCapacity - rabbits[i-1] - kangaroos[i-1] * foodNeed) / rabbitCapacity
        kangaroos[i] = kangaroos[i-1] + kangarooVelocity * kangaroos[i-1] * (kangarooCapacity - kangaroos[i-1] - rabbits[i-1] / foodNeed) / kangarooCapacity
        print(rabbits[i])
    
    plt.plot(time, rabbits, time, kangaroos)
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.show()

# Function calls
rabbitKangaroo()
rabbitGrowth()
