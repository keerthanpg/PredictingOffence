from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import pickle

with open('X_train.pkl', 'rb') as f:
	X_train = pickle.load(f)


with open('Y_train.pkl', 'rb') as f:
	Y_train = pickle.load(f)


with open('X_test.pkl', 'rb') as f:
	X_test = pickle.load(f)

with open('Y_test.pkl', 'rb') as f:
	Y_test = pickle.load(f)
print(type(Y_train[1]))
print(X_train[1])
print(type(X_train[1]))

for i in range(len(X_train[1])):
	print(type(X_train[1][i]))

clf = MLPClassifier(solver='lbfgs', alpha=1e-3, hidden_layer_sizes=(2, 3), random_state=1)
clf.fit(X_train[1:], Y_train[1:]) 
Y_result=clf.predict(X_test[1:])
print(Y_result)

correct=0
wrong=0

for i in range(len(Y_result)):
	if Y_result[i]==Y_test[i+1]:
		correct+=1
	else:
		wrong+=1

print(correct)
print(wrong)

print(correct/(correct+wrong))
#highest accuracy=0.4056004532848239
