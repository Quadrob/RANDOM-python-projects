import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

#K-Means clustering implementation

# Define a function that computes the distance between two data Points
def distance(x1, y1, x2, y2):
    distance = ((((x1 - x2)**2) + ((y1 - y2)**2))**0.5)
    return distance

# Define a function that reads data in from the csv files
def readFile(File):
    csvFile = pd.read_csv(File)
    return csvFile

#function to plot on a gragh
def plot(x, y, centroidPoint):
    colorMap = {0:'red', 1: 'blue', 2: 'green', 3: 'yellow', 4: 'orange'}
    plt.scatter(x, y, c = 'black', s = 7)
    plt.scatter(centroidPoint[0], centroidPoint[1], color = colorMap[centroid], s = 150, marker = '*')

# Write the initialisation procedure
#get file
userFile = "dataBoth.csv"
#userFile = "data2008.csv"
#userFile = "data1953.csv"
csvFile = readFile(userFile)
print("\n\t File Preview : \n")
print(csvFile.head())

#set values using iloc from files
countries = csvFile.iloc[:,0]
birthRate = csvFile.iloc[:,1].values
lifeExpect = csvFile.iloc[:,2].values
 
lengthOfFile = len(birthRate)#get lenght of data
#get amount of centroid points
numOfCentroids = 2
centroidPoints = {}
userDefinedNumOfCentroids = int(input("\n\nPlease enter the number of numOfCentroids : "))
if (userDefinedNumOfCentroids > 5):
    print("invalid amount: value too high, reverting to default [2]")
elif (userDefinedNumOfCentroids < 2):
    print("invalid amount: value too low, reverting to default [2]")
else:
    numOfCentroids = userDefinedNumOfCentroids
     
#assign random points for each centroid from data and plot the data
print("\nThe centroid Start positions are : ")
for centroid in range(numOfCentroids):
    centroidPoints[centroid] = [random.choice(birthRate), random.choice(lifeExpect)]
    print("\nIntial Centroid Points " + str(centroid) + " = ")
    print(centroidPoints[centroid])
    centroidPoint = centroidPoints[centroid]
    plot(birthRate, lifeExpect, centroidPoint)
     
plt.show()

#get iterations
userIterations = int(input("\nPlease enter the number of iterations : "))

# Implement the k-means algorithm, using appropriate looping

#for loop to run through user iterations and calculate k means, it gets the distance from each point
#and saves the point under its nearest centroid
for iteration in range(userIterations):
    print("\nIteration Number " + str(iteration))
    #declare variabls and lists
    closestPoints = {}
    x_points = {}
    y_points = {}
    newCentroids = []
    sumDistance = {}
 
    #for loop to create tuples in x + y points
    for i in range(numOfCentroids):
        x_points[i] = []
        y_points[i] = []
        sumDistance[i] = []
            
    #calculate the difference and store the nearest
    for j in range(lengthOfFile):
        distanceBetween = 0.0
        nearestTo = 1000000
        for centroid in range(numOfCentroids):
            centroidPoint = centroidPoints[centroid]
            #get distance
            distanceBetween = (distance(birthRate[j], lifeExpect[j], centroidPoint[0], centroidPoint[1]))
            #save nearest point
            if (distanceBetween < nearestTo):
                nearestTo = distanceBetween
                closestPoints[j] = centroid
        #store all the squared distances to dict
        sumDistance[closestPoints[j]].append(nearestTo)
     
    #add all the cordinates to x/y list
    for point in (closestPoints):
        for centroid in range(numOfCentroids):
            if (closestPoints[point] == centroid):
                x_points[centroid].append(birthRate[point])
                y_points[centroid].append(lifeExpect[point]) 
          
    #average of x points
    for points in x_points:
        x_points[points] = sum(x_points[points]) / len(x_points[points])
        
    #average of y points
    for points in y_points:
        y_points[points] = sum(y_points[points]) / len(y_points[points])
    
    #add all points togetther   
    for a in range(numOfCentroids):
        sumDistance[a] = sum(sumDistance[a])

    #set new centroid postions using x/y points and print total squared distance 
    for centroid in range(numOfCentroids):
        centroidPoint = centroidPoints[centroid]
        centroidPoint[0] = x_points[centroid]
        centroidPoint[1] = y_points[centroid]
        print("\nThe Sum of Squared Diffrences for Centroid " + str(centroid) + " is : ")
        print(sumDistance[centroid])
        plot(birthRate, lifeExpect, centroidPoint)

    plt.show()

print("\n\n\tInformation : \n")

#declare a dict and save diferent empty tuples for each centroid to store num of countries
numOfCountries = {}   
for i in range(numOfCentroids):
    numOfCountries[i] = []

#nessted for loop to add countries for each centroid 
for point in (closestPoints):
    for centroid in range(numOfCentroids):
        if (closestPoints[point] == centroid):
            numOfCountries[centroid].append(1)
            
#print out number of countries for each centroid
for points in numOfCountries:
    numOfCountries[points] = sum(numOfCountries[points])
    print("\nThe number of countries belonging to centroid " + str(points) + " is : ")
    print(numOfCountries[points])

#print out the average BR / LE for each centroid from x/y points
for centroid in range(numOfCentroids):
    print("\nThe Average Birth Rate for centroid " + str(centroid) + " is : ")
    print(x_points[centroid])
    print("\nThe Average life Expectancy for centroid " + str(centroid) + " is : ")
    print(y_points[centroid])

##declare a dict and save diferent empty tuples for each centroid to store num of countries
countryNames = {}   
for i in range(numOfCentroids):
    countryNames[i] = []
    
#stores the country names for each centroid in dict
for point in (closestPoints):
    for centroid in range(numOfCentroids):
        if (closestPoints[point] == centroid):
            countryNames[centroid].append(countries[point])

#print out the countries
for centroid in range(numOfCentroids):
    print("\nThe countries that fall under centroid " + str(centroid) + " is : ")
    print(countryNames[centroid])

#final plot of the graph
for point in (closestPoints):
    for centroid in range(numOfCentroids):
        colorMap = {0:'red', 1: 'blue', 2: 'green', 3: 'yellow', 4: 'orange'}
        if (closestPoints[point] == centroid):
            plt.scatter(birthRate[point], lifeExpect[point], c = colorMap[centroid], s = 7)

        centroidPoint = centroidPoints[centroid]
        plt.scatter(centroidPoint[0], centroidPoint[1], color = colorMap[centroid], s = 150, marker = '*')

plt.show()          