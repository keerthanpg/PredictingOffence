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


Y_result=[]
for i in range(1,len(Y_test)):
	Y_result.append(1)#ID of grand larceny
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
print(accuracy_score(Y_test[1:], Y_result))
#highest accuracy=0.4056004532848239
