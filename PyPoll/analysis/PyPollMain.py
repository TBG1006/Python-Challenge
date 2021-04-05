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

    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

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

#set dictionary to accept list values
#pollDataDict = {"ID":0,"COUNTY":"Test","CANDIDATE":"Test"}

#***********add list values to the dictionary *****not needed
pollDataDict["Khan"] = khanCount
pollDataDict["Correy"] = correyCount
pollDataDict["Li"] = liCount
pollDataDict["O'Tooley"] = otooleyCount

winner = max(pollDataDict, key=pollDataDict.get)
print(winner)
khanPercent = len(khanCount) / totalVotes * 100
correyPercent = len(correyCount) / totalVotes * 100
liPercent = len(liCount) / totalVotes * 100
otooleyPercent = len(otooleyCount) / totalVotes * 100
#print(khanPercent)  
#print(correyPercent) 
#print(liPercent)  
#print(otooleyPercent) 


print("Election Results:")
print("----------------------------------------------")
print(f'Total Votes: {totalVotes}')
print("----------------------------------------------")
print(f'Khan: {khanPercent:.3F}% ({len(khanCount)})')
print(f'Correy: {correyPercent:.3F}% ({len(correyCount)})')
print(f'Li: {liPercent:.3F}% ({len(liCount)})')
print(f"O'Tooley: {otooleyPercent:.3F}% ({len(otooleyCount)})")
print(f'WINNER: {winner}')

# Output Files
output_path = os.path.join('PyPoll', 'Analysis', 'PyPollOutput.csv')

with open (output_path, 'w', newline='') as csvfile:

    #csvwriter = csv.writer(csvfile, delimiter=',')
    csvfile.write("Election Results:")
    csvfile.write("\n")
    csvfile.write("-------------------------------------------")
    csvfile.write("\n")
    csvfile.write(f"Total Votes: {totalVotes}")
    csvfile.write("\n")
    csvfile.write(f'Khan: {khanPercent:.3F}% ({len(khanCount)})')
    csvfile.write("\n")
    csvfile.write(f'Correy: {correyPercent:.3F}% ({len(correyCount)})')
    csvfile.write("\n")
    csvfile.write(f'Li: {liPercent:.3F}% ({len(liCount)})')
    csvfile.write("\n")
    csvfile.write(f"O'Tooley: {otooleyPercent:.3F}% ({len(otooleyCount)})")
    csvfile.write("\n")
    csvfile.write(f'WINNER: {winner}')