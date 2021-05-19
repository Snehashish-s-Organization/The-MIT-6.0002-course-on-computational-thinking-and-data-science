"""
Implements the idea of stochastic thinking

"""
import random

def randomchoice():
    number = random.randint(1, 6)
    return number

def textrandom():
    for i in range(100):
        print(randomchoice())
        
def calculateProbability(no_of_times, no_of_inpiuts):
    number = 1/no_of_inpiuts**no_of_times
    
    print(number)
    
    
calculateProbability(3, 3)