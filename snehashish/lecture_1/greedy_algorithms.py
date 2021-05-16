"""
Work from the first Optimization problem which
happens to be the knapsack problem. The burglar 
algorith needs to be implemented!

"""

# creating a class Item for every Item in the house
class Item(object):
    # passing the parameters and storing them into the class
    def __init__(self, name, value, weight):
        self.name = name
        self.weight = weight
        self.value = value

    # defining a function to return the value of the Item
    def getValue(self):
        return self.value

    # defining a function to return the weight of the Item
    def getWeight(self):
        return self.weight

    # definig a function to return the name of the Item
    def getName(self):
        return self.name

    def __str__(self):
        return str([self.name, self.weight, self.value])


# creating a function that returns the value of a given item
def value(item):
    return item.getValue()


# creating a function that returns the inverse weight of a given item
# Which is needed while implementing the greedy algorithm by weight
def weight_inverse(item):
    return 1.0/item.getWeight()


# creating a function that returns the value to weight ratio of a given item
def density(item):
    return item.getValue()/item.getWeight()


# creating a the main greedy algorithm which is an efficient algorithm
def greedy(items, max_weight, key_functions):
    # creating a copy of the items list so that we don not mess any thing up
    items_copy = sorted(items, key = key_functions, reverse = True)

    # Defining the total_value and the total weight
    # Which will be changed to calculate the total value and weight after the algorithm has been used
    total_value = 0
    total_weight = 0

    # defining a list that will contain the end result
    result = []

    # iteration over the list of items and seeing if we can fit more into the knapsack,
    # it checks by seeing if the total weight exceeds the max weight and if not,
    # puting the item into the knapsack and increasing the total value and weight
    for i in range(len(items_copy)):
        # This is the man heart of the algorithm where it checks if the total weight exceeds the max weight
        if (total_weight + items_copy[i].getWeight()) <= max_weight:
            # adding the item to the knapsack
            result.append(items_copy[i])
            # increasing the values
            total_value += items_copy[i].getValue()
            total_weight += items_copy[i].getWeight()
    # returning a tuple containing the end result and the total value of items fit into the knapsack
    return (result, total_value)


def build_items():
    # Building the items in the house items
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    #creating a list of items that will act as the house(bassically store items into it)
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    # returning the Items list
    return Items


# defining a function to test the greedy algorithm
def test_greedy(items, max_weight, key_function):
    # getting the result list and total_value and storing them into the variables
    taken, val = greedy(items, max_weight, key_function)
    print("Total value of items taken is", val)
    for item in taken:
        print('    ', item)


# Using the test greedy to actually test the greedy algorithm
def Main(max_weight =10):
    # getting the items by using the build_items function defined above
    items = build_items()

    # printing out the end results if the value is the main point 
    print("Use greedy by value to fill knapsack of size", max_weight)
    test_greedy(items, max_weight, value)

    # printing out the end results if the weight is the main point
    print("Use greedy by weight to fill knapsack of size", max_weight)
    test_greedy(items, max_weight, weight_inverse)

    # printing out the end results if the value to weight ratio is the main point
    print("Use greedy by density to fill knapsack of size", max_weight)
    test_greedy(items, max_weight, density)








