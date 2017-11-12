import csv
import pickle



exampleFile = open('NYPD_7_Major_Felony_Incidents_train.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
keys=exampleData[0]
print(len(exampleData))
print(exampleData[1][10])

offenceID={} #maps offence to a number 1D
j=0
sectorID={}#maps sector to a number 1D
k=0
boroughID={}#maps borough to an ID
l=0
jurisdictionID={}#maps jurisdiction to an ID
m=0

dayofweekID={'Sunday':1,'Monday':2, 'Tuesday':3, 'Wednesday':4, 'Thursday':5, 'Friday':6, 'Saturday':7} #maps day of week to an ID
monthID={'Jan':1,'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12} #maps month to an ID


exampleData[0].append('OffenceID')
exampleData[0].append('dayofweekID')
exampleData[0].append('monthID')
exampleData[0].append('sectorID')
exampleData[0].append('boroughID')
exampleData[0].append('jurisdictionID')


for i in range(1,len(exampleData)):
	if(exampleData[i][10] not in offenceID):
		j=j+1
		offenceID[exampleData[i][10]]=j
		exampleData[i].append(offenceID[exampleData[i][10]])
	else:
		exampleData[i].append(offenceID[exampleData[i][10]])

	if(exampleData[i][2] not in dayofweekID):
		print("Exception! Day not in day of weekID")
		print(exampleData[i][2])
		break
	else:
		exampleData[i].append(dayofweekID[exampleData[i][2]])

	if(exampleData[i][3] not in monthID):
		print("Exception! Day not in day of monthID")
		print(exampleData[i][3])
		break
	else:
		exampleData[i].append(monthID[exampleData[i][3]])


	if(exampleData[i][11] not in sectorID):
		k=k+1
		sectorID[exampleData[i][11]]=k
		exampleData[i].append(sectorID[exampleData[i][11]])
	else:
		exampleData[i].append(sectorID[exampleData[i][11]])

	if(exampleData[i][13] not in boroughID):
		l=l+1
		boroughID[exampleData[i][13]]=l
		exampleData[i].append(boroughID[exampleData[i][13]])
	else:
		exampleData[i].append(boroughID[exampleData[i][13]])

	if(exampleData[i][14] not in jurisdictionID):
		m=m+1
		jurisdictionID[exampleData[i][14]]=m
		exampleData[i].append(jurisdictionID[exampleData[i][14]])
	else:
		exampleData[i].append(jurisdictionID[exampleData[i][14]])

print(sectorID)
print(boroughID)
print(jurisdictionID)

print(exampleData[0])

Y_train=[]
X_train=[]

Y_train.append(exampleData[0][19])
X_train.append([exampleData[0][6], exampleData[0][20], exampleData[0][21], exampleData[0][5], exampleData[0][24], exampleData[0][15], exampleData[0][16]])


for i in range(1,len(exampleData)):
	Y_train.append(int(exampleData[i][19]))
	X_train.append([int(exampleData[i][6]), int(exampleData[i][20]), int(exampleData[i][21]),  int(exampleData[i][5]), int(exampleData[i][24]), int(exampleData[i][15]), int(exampleData[i][16])])

print(X_train[0])
print(Y_train[0])
print(offenceID)

with open('X_train.pkl', 'wb') as outX:
    pickle.dump(X_train, outX)

with open('Y_train.pkl', 'wb') as outY:
    pickle.dump(Y_train, outY)


with open('offenceID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)

with open('sectorID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)


with open('boroughID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)


with open('jurisdictionID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)






