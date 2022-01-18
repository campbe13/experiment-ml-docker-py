'''
simple example using Classification to determine 
when to wear a coat 

p.campbell
2022-01-13

TODO: use inline data instead of CSV makes it more obvious
this: generate a larger dataset 100x random 11-35 & 10 to -30 (precision 2 decimals)
refs
https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
'''

import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import random

# generate data set
X = list()
y = list()
# 100 >=10
for i in range(5000):
    # random float 2 decimal points
    z = round(random.uniform(10.0, 35.0), 3)
    X.append([z])
    y.append('none')
# 100 <10
for i in range(5000):
    # random float 2 decimal points
    z = round(random.uniform(9.99, -35.0), 3)
    X.append([z])
    y.append('coat')
for i in range(0,9):
    X.append([i])
    y.append('coat')
#print("X ",X)
#print("y ",y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25) 
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test) 

# Use the KNN classifier to fit data:
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(X_train, y_train) 

# Predict y data with classifier: 
y_predict = classifier.predict(X_test)
print ("given ",X_test)
print ("predict ",y_predict)
#test2 = [[25,4, -20, 14]]
# note it will predict none for 4 degrees, training set is insufficient
test2 = [[35], [-4], [4]]
print ("given ", test2 )
print ("predict ", classifier.predict(test2))
test2 = [[-25]]
print ("given ", test2 )
print ("predict ", classifier.predict(test2))
for i in range(30):
    test2 = [[round(random.uniform(-35.0, 35.0), 3)]]
    result = classifier.predict(test2)
    #print ("given ", test2, " predict ", result) 
    if result == 'coat':
        print(f'When it\'s {test2[0][0]} wear a {result[0]}')
    else:
        print(f'When it\'s  {test2[0][0]} wear  {result[0]}')

# Print results: 
'''
confusion matrix: s a summarized table of the number of correct and incorrect predictions (or actual and predicted values) yielded by a classifier (or classification model) for binary classification tasks. 

'''
#print("confusion matrix", confusion_matrix(y_test, y_predict))
#print("classification report\n", classification_report(y_test, y_predict)) 