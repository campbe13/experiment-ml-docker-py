'''
simple example using Linear Regression to estimate the values for
f(x,y,z)  = x + 2y + 3z
p.campbell
2022-01-06

refs
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
https://www.tutorialspoint.com/scikit_learn/scikit_learn_estimator_api.htm
'''

def predict(test, model) :
    return model.predict(X=test)
    
from sklearn.linear_model import LinearRegression

from random import randint
LIMIT = 1000  # max for x, y, z
COUNT = 100   # number of values in the training set

# input values x, y, z of  f(x,y,z)  
TRAIN_INPUT = list()
# the result of f(x,y,z)
TRAIN_RESULT = list()
for i in range(COUNT):
    # generate random numbers
    x = randint(0, LIMIT)
    y = randint(0, LIMIT)
    z = randint(0, LIMIT)
    TRAIN_INPUT.append([x, y, z])
    # result of the algebraeic function
    result = x + (2*y) + (3*z)
    TRAIN_RESULT.append(result)
'''
create the fitted estimator, using the training data
fit the model to the data   (train it)
features: x, target: y
'''
model = LinearRegression(n_jobs=-1).fit(X=TRAIN_INPUT, y=TRAIN_RESULT) 
#print("model coefficients {}  ".format(model.coef_))
#print("model params {} ".format(model.get_params()))

# Now use the model
# test set  f(5, 6, 10)  (result should be 5+12+30 or 47)
test = [[ 5, 6, 10 ]]
'''
estimate = model.predict(X=test)
# resul
print("Result {} ".format(estimate))
'''
print("using the model:")
result =  predict(test, model)
print("result: {} from x,y,z values  {} ".format(result[0], test))
result =  predict([[10, 10, 10]], model)
print("result: {} from x,y,z values  {}".format(result[0], [[10,10,10]]))
result =  predict([[3, 2, 1]], model)
print("result: {} from x,y,z values  {}".format(result[0], [[3,2,1]]))