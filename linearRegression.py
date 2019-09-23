import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

#slope function
def gradient(x, y):
#theres something going wrong with this equation (i think divison by 0)
   gradient = ((np.mean(x) * np.mean(y)) - np.mean(x * y))/((np.mean(x)**2) - np.mean(x**2))
   return gradient

#intersect function
def yIntersect(x, y, m):
   yIntersect = np.mean(y) - m * np.mean(x)
   return yIntersect
   
def plot_regression_line(x, y, slope, yInt): 
    # predicted response vector 
    yPredict = (slope * x + yInt)
  
    # plotting the regression line 
    plt.plot(x, yPredict, color='blue', linewidth=3, label='Best fit line') 
  
    plt.legend()

    plt.savefig('plot.png')
    plt.show()

#collecting data   
diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20].flatten()
diabetes_y_train = diabetes.target[:-20]

diabetes_X_test = diabetes_X[-20:]
diabetes_y_test = diabetes.target[-20:]

slope = gradient(diabetes_X_train, diabetes_y_train)
yIntersept = yIntersect(diabetes_X_train, diabetes_y_train, slope)
print("Estimated coefficients: \nSlope = " + str(slope) + "\nY Intersect = " + str(yIntersept))

#ploting data
plt.scatter(diabetes_X_test,  diabetes_y_test,  color='green', label="Test")
plt.scatter(diabetes_X_train,  diabetes_y_train,  color='red', label ='Training')

plot_regression_line(diabetes_X_train, diabetes_y_train, slope, yIntersept)

