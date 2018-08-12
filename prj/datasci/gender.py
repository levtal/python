#!/usr/bin/env python3
#   pip   install -U scikit-learn
#   pip install matplotlib
# https://github.com/llSourcell/gender_classification_challenge
#  C:\Users\gilfm\AppData\Local\Programs\Python\Python35\Scripts\pip


from sklearn import tree
#from sklearn.tree import DecisionTreeClassifier
from sklearn import gaussian_process
from sklearn import neural_network
clf = tree.DecisionTreeClassifier()
rb = gaussian_process.GaussianProcessClassifier()
nu = neural_network.MLPClassifier
# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
prediction = clf.predict([[190, 70, 43]])

# CHALLENGE compare their reusults and print the best one!

print('DecisionTreeClassifier= ',prediction)

rb = rb.fit(X, Y)
prediction = rb.predict([[190, 70, 43]])
print('gaussian_process = ',prediction)

#nu = nu.fit(X, Y)
#prediction = nu.predict([[190, 70, 43]])
#print('neural_network = ',prediction)

 