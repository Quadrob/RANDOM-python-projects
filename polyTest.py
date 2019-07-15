import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#polynomial regression modle for the age of children in a school 
#and the average hight of each age group in the school

# My Training sets
X_train =[[10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]#age of children in school
y_train =[[121], [124], [128], [135], [145], [159], [172], [181], [186], [189]]#average hight of children in that age group in school

# My Testing sets
X_test = [[12], [19], [10], [12], [18], [14], [17], [19], [16], [15]]#age of Child
y_test = [[129], [190], [121], [128], [186], [144], [181], [188], [171], [162]]#hight of child

# Train the Linear Regression model and plot a prediction
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#linspace gets 100 points between 10 and 19
xx = np.linspace(10, 19, 150)
#xx.shape[0] gets the rows in xx and 1 is colums and reshape turns it into an array
#of 100 rows and 1 colum and then yy is predicted
yy = regressor.predict(xx.reshape(xx.shape[0], 1))
plt.plot(xx, yy)

# Set the degree of the Polynomial Regression model
quadratic_featurizer = PolynomialFeatures(degree=2)

# This preprocessor transforms an input data matrix into a new data matrix of a given degree
#Transformation [a,b] = [1, a, b, ab, a^2, b^2]
#Transformation [a,b,c] = [1, a, b, c, ab, bc, ac, a^2, b^2, c^2]
#in this case [a] = [1, a, a^2]
X_train_quadratic = quadratic_featurizer.fit_transform(X_train)
X_test_quadratic = quadratic_featurizer.transform(X_test)

# Train and test the regressor_quadratic model
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# Plot the graph
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.title('Average hight of chilren regressed on Age group')
plt.xlabel('Child Age Group')
plt.ylabel('Average hight in cm')
plt.axis([9, 20, 100, 200])
plt.grid(True)
plt.scatter(X_train, y_train)
plt.savefig('plot.png')
plt.show()
print ("X_train = ")
print (X_train)
print ("\nX_train_quad = ")
print (X_train_quadratic)
print ("\nX_test = ")
print (X_test)
print ("\nX_test_quad = ")
print (X_test_quadratic)