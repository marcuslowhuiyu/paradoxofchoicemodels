import numpy as np
import matplotlib.pyplot as plt
import random

choices = []

def generateChoice(n, minVal, maxVal):
    """
    Generates an array of choices with corresponding satisfaction levels

    :param n: int
        Number of choices available
    :param minVal: double
        Minimum satisfaction level of each choice
    :param maxVal: double
        Maximum satisfaction level of each choice
    """
    choices.clear()
    for i in range(n):
        choices.append(random.randint(minVal, maxVal))


def findBest(choices, cost):
    """
    Finds the best possible choice amongst all choices

    :param choices: arr
        Array containing the choices and their corresponding satisfaction levels
    :param cost: double
        "Cost of deciding"
        Used to representing the cost of not coming to a decision and to look for alternatives
    :return: double
        The best possible satisfaction level amongst all the choices
    """
    currBest = 0
    currCost = 0
    for i in choices:
        currCost += cost
        if i > currBest:
            currBest = i
    return currBest - currCost

def findGoodEnough(choices, cost, target):
    """
    Finds the best possible choice until the target satisfaction is found or exceeded

    :param choices: arr
        Array containing the choices and their corresponding satisfaction levels
    :param cost: double
        "Cost of deciding"
        Used to represent the cost of not coming to a decision and to look for alternatives
    :param target: double
        Target satisfaction level to be achieved
    :return: double
        The first choice that exceeds/meets the target satisfaction level
        If no choice exceeds/meets the target, returns the highest satisfaction level amongst the choices
    """
    currBest = 0
    currCost = 0
    for i in choices:
        currCost += cost
        if i >= target:
            currBest = i
            break
        elif i > currBest:
            currBest = i
    return currBest - currCost


def maximiser(arr, numOfChoices, runs, cost, minVal, maxVal):
    """
    Simulates a maximising agent

    :param arr: arr
        Array that stores the result
        Each index represents the number of choices
        Each value represents the result at that corresponding number of choices
    :param numOfChoices: int
        The maximum number of choices available
    :param runs: int
        Number of runs of each number of choice
    :param cost: double
        "Cost of deciding"
        Used to represent the cost of not coming to a decision and to look for alternatives
    :param minVal: double
        Minimum possible satisfaction value of each choice
    :param maxVal: double
        Maximum possible satisfaction value of each choice
    :return temp: arr
        Final results of the simulation
    """
    for i in range(numOfChoices):
        arr.append(0)
        for j in range(runs):
            generateChoice(i, minVal, maxVal)
            arr[i] = arr[i] + findBest(choices, cost)
    result = [x / runs for x in arr]
    return result

def satisficer(arr, numOfChoices, runs, cost, minVal, maxVal):
    """
    Simulates a satisficing agent

    :param arr: arr
        Array that stores the result
        Each index represents the number of choices
        Each value represents the result at that corresponding number of choices
    :param numOfChoices: int
        The maximum number of choices available
    :param runs: int
        Number of runs of each number of choice
    :param cost: double
        "Cost of deciding"
        Used to represent the cost of not coming to a decision and to look for alternatives
    :param minVal: double
        Minimum possible satisfaction value of each choice
    :param maxVal: double
        Maximum possible satisfaction value of each choice
    """
    for i in range(numOfChoices):
        arr.append(0)
        for j in range(runs):
            generateChoice(i, minVal, maxVal)
            targetSatisfaction = random.randint(minVal, maxVal)
            arr[i] = arr[i] + findGoodEnough(choices, cost, targetSatisfaction)
    result = [x / runs for x in arr]
    return result

# Tests

maxResults = []
satisResults = []

maxResults = maximiser(maxResults, 200, 1000, 1, 0, 100)
satisResults = satisficer(satisResults, 200, 1000, 1, 0, 100)

max = np.array(maxResults)
satis = np.array(satisResults)
plt.plot(max, color='r', label='maximiser')
plt.plot(satis, color='b', label='satisficer')
plt.title("Maximiser versus Satisficer")
plt.ylabel("Satisfaction")
plt.xlabel("Number of Choices")
plt.legend()
plt.show()