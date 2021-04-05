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
        elif i == "Li":
            liCount.append(1)
        elif i == "O'Tooley":
            otooleyCount.append(1)

totalVotes = len(voterIDList)

print(len(khanCount))  
#print(len(correyCount)) 
#print(len(liCount))  
#print(len(otooleyCount))          


#set dictionary to accept list values
#pollDataDict = {"ID":0,"COUNTY":"Test","CANDIDATE":"Test"}

#***********add list values to the dictionary *********I don't think I need any of this section 
pollDataDict["Khan Votes"] = khanCount
pollDataDict["Correy Votes"] = correyCount
pollDataDict["Li Votes"] = liCount
pollDataDict["O'Tooley Votes"] = otooleyCount

print(f'{len(pollDataDict["Khan Votes"])}')
#***********add list values to the dictionary *********I don't think I need any of this section