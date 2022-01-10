'''
simple example using Linear Regression to determine 
when to wear a coat 

p.campbell
2022-01-010

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

TRAIN_SET = [  [ [27,0], "no coat"], [[21,0], "no coat"], [[15,0], "no coat"], 
               [[7,0], "coat"], [[5,0], "coat"], [[-5,0], "coat"]]
TRAIN_INPUT = list()
TRAIN_RESULT = list()
for data in TRAIN_SET:
    print(data[0])
    print(data[1])
    TRAIN_INPUT.append([data[0]])
    if data[1] == 'coat': 
        TRAIN_RESULT.append(1)
    else:
        TRAIN_RESULT.append(0)
'''
create the fitted estimator, using the training data
fit the model to the data   (train it)
features: x, target: y
'''
model = LinearRegression(n_jobs=-1).fit(X=TRAIN_INPUT, y=TRAIN_RESULT) 
#print("model coefficients {}  ".format(model.coef_))
print("model params {} ".format(model.get_params()))

# Now use the model
test = 10

estimate = model.predict(X=test)
print("Result {} ".format(estimate))
'''
print("using the model:")
result =  predict(test, model)
print("result: {} from x,y,z values  {}".format(result[0], test))
result =  predict([[10, 10, 10]], model)
print("result: {} from x,y,z values  {}".format(result[0], [[10,10,10]]))
result =  predict([[3, 2, 1]], model)
print("result: {} from x,y,z values  {}".format(result[0], [[3,2,1]]))
'''