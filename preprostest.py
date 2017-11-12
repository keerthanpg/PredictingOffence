import csv
import pickle



exampleFile = open('NYPD_7_Major_Felony_Incidents_test.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
keys=exampleData[0]
print(len(exampleData))
print(exampleData[1][10])

with open('offenceID.pkl', 'rb') as f:
	offenceID = pickle.load(f)


with open('sectorID.pkl', 'rb') as f:
	sectorID = pickle.load(f)
k=len(sectorID)

with open('boroughID.pkl', 'rb') as f:
	boroughID = pickle.load(f)
l=len(boroughID)

with open('jurisdictionID.pkl', 'rb') as f:
	jurisdictionID = pickle.load(f)
m=len(jurisdictionID)

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
		print("Exception! Offence not in day of OffenceID")
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
		print("sector="+str(exampleData[i][11]))
		k=k+1
		sectorID[exampleData[i][11]]=k
		exampleData[i].append(sectorID[exampleData[i][11]])
	else:
		exampleData[i].append(sectorID[exampleData[i][11]])

	if(exampleData[i][13] not in boroughID):
		print("borough="+str(exampleData[i][13]))
		l=l+1
		boroughID[exampleData[i][13]]=l
		exampleData[i].append(boroughID[exampleData[i][13]])
	else:
		exampleData[i].append(boroughID[exampleData[i][13]])

	if(exampleData[i][14] not in jurisdictionID):
		print("jurisdiction="+str(exampleData[i][14]))
		m=m+1
		jurisdictionID[exampleData[i][14]]=m
		exampleData[i].append(jurisdictionID[exampleData[i][14]])
	else:
		exampleData[i].append(jurisdictionID[exampleData[i][14]])
	

print(sectorID)
print(boroughID)
print(jurisdictionID)
print(exampleData[0])

Y_test=[]
X_test=[]

Y_test.append(exampleData[0][19])
X_test.append([exampleData[0][6], exampleData[0][20], exampleData[0][21], exampleData[0][5], exampleData[0][24], exampleData[0][15], exampleData[0][16]])


for i in range(1,len(exampleData)):
	Y_test.append(int(exampleData[i][19]))
	X_test.append([int(exampleData[i][6]), int(exampleData[i][20]), int(exampleData[i][21]), int(exampleData[i][5]), int(exampleData[i][24]), int(exampleData[i][15]), int(exampleData[i][16])])

print(X_test[0])
print(Y_test[0])


with open('X_test.pkl', 'wb') as outX:
    pickle.dump(X_test, outX)

with open('Y_test.pkl', 'wb') as outY:
    pickle.dump(Y_test, outY)

with open('sectorID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)


with open('boroughID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)


with open('jurisdictionID.pkl', 'wb') as out:
    pickle.dump(offenceID, out)







