import random

"""
Implementing the Decision tree


"""
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

def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def fastMaxVal(toConsider, avail, memo = {}):
    """Assumes toConsider a list of subjects, avail a weight
         memo supplied by recursive calls
       Returns a tuple of the total value of a solution to the
         0/1 knapsack problem and the subjects of that solution"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Explore right branch only
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
                 fastMaxVal(toConsider[1:],
                            avail - nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],
                                                avail, memo)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print('Menu contains', len(foods), 'items')
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print('   ', item)
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items
for numItems in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
    numCalls = 0
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 20, fastMaxVal)
    print('Number of calls =', numCalls)




