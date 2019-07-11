from sklearn import tree

features = []
labels = []
clf = tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print ( clf.predict ([[]]) )