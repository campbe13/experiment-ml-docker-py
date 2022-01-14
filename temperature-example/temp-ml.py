'''
simple example using Classification to determine 
when to wear a coat 

p.campbell
2022-01-13

TODO: use inline data instead of CSV makes it more obvious

refs
https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a
https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
'''

import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

cols = ['temperature', "wear coat"]
data = pandas.read_csv(r'temp-coat.csv',names=cols)
data.head()
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

print("X ",X)
print("y ",y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) 
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

# Print results: 

print("confusion matrix", confusion_matrix(y_test, y_predict))
print("classification report\n", classification_report(y_test, y_predict)) 