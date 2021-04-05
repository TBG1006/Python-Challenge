import os
import csv

#Dict to hold the CSV columns as lists
pollDataDict = {}

# Set lists to accept data from csv
voterIDList = []
countyList = []
candidateList = []
khanCount = []
correyCount = []
liCount = []
otooleyCount = []


csvpath = os.path.join('PyPoll', 'Resources', 'PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        voterIDList.append(int(row[0]))
        countyList.append(row[1])
        candidateList.append(row[2])
    
    for i in candidateList:
        if i == "Khan":
            khanCount.append(1)
        elif i == "Correy":
            correyCount.append(1)

print(len(khanCount))  
print(len(correyCount))           
#print(voterIDList[8])
#print(countyList[8])
#print(candidateList[8])

#set dictionary to accept list values
pollDataDict = {"ID":0,"COUNTY":"Test","CANDIDATE":"Test"}

#add list values to the dictionary
pollDataDict["ID"] = voterIDList
pollDataDict["COUNTY"] = countyList
pollDataDict["CANDIDATE"] = candidateList

totalVotes = len(voterIDList)
#print(totalVotes)

#print(f'{pollDataDict["CANDIDATE"][8]}')