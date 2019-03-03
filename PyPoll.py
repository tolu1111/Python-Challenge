#Import Dependencies perform certain functions in python
import os
import csv

# define where the data is located
electiondata = os.path.join("Resources", "election_data.csv")

# define empty lists for the different contestants to store their recorded votes
TotalVotes = []
TotalKhan = []
TotalCorrey = []
TotalLi = []
TotalOTooley = []

# Read csv file 
with open(electiondata, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)
# calculate the values for the different candidates
# store respective values in appropraite lists created earlier  

    for row in csvreader:
        TotalVotes.append((row[2]))
    
        if (row[2]) == "Khan":
            TotalKhan.append((row[2]))
        elif (row[2]) == "Correy":
            TotalCorrey.append((row[2]))
        elif (row[2]) == "Li":
            TotalLi.append((row[2]))
        else:
            TotalOTooley.append((row[2]))
#calculate voting totals for each candidate
KhanResults = int(len(TotalKhan))
CorreyResults = int(len(TotalCorrey))
LiResults = int(len(TotalLi))
OTooleyResults =int(len(TotalOTooley))

#calculate the percentage votes for each candidate with respect to total votes
Khan_percent_votes = (int(len(TotalKhan))/int(len(TotalVotes)))
Correy_percent_votes = (int(len(TotalCorrey))/int(len(TotalVotes)))
Li_percent_votes = (int(len(TotalLi))/int(len(TotalVotes)))
OTooley_percent_votes = (int(len(TotalOTooley))/int(len(TotalVotes)))


#Define Election results
ElectionResults = [KhanResults, CorreyResults, LiResults, OTooleyResults]

#Calculate Election winner
for winner in ElectionResults:  
    if max(ElectionResults) == KhanResults:
            ElectionWinner = "Khan"
    elif max(ElectionResults) == CorreyResults:
            ElectionWinner = "Correy"
    elif max(ElectionResults) == LiResults:
            ElectionWinner = "Li"
    else: 
            ElectionWinner = "O'Tooley"
    


# print the Election Results, total votes and percentages for each voter

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {len(TotalVotes)}")
print("-----------------------------------")
print(f'Khan: {(format((Khan_percent_votes), ".3%"))} ({len(TotalKhan)})')
print(f'Correy: {(format((Correy_percent_votes), ".3%"))} ({len(TotalCorrey)})')
print(f'Li: {(format((Li_percent_votes), ".3%"))} ({len(TotalLi)})')
print(f"O'Tooley: {(format((OTooley_percent_votes), '.3%'))} ({len(TotalOTooley)})")

print("-----------------------------------")
print(f"Winner: {ElectionWinner}")

print("-----------------------------------")

#export text file
p = open("PyPoll.txt","w+")
p.write("Election Results\n")
p.write("-----------------------------------\n")
p.write(f"Total Votes: {len(TotalVotes)}\n")
p.write("-----------------------------------\n")
p.write(f'Khan: {(format((Khan_percent_votes), ".3%"))} ({len(TotalKhan)})\n')
p.write(f'Correy: {(format((Correy_percent_votes), ".3%"))} ({len(TotalCorrey)})\n')
p.write(f'Li: {(format((Li_percent_votes), ".3%"))} ({len(TotalLi)})\n')
p.write(f"O'Tooley: {(format((OTooley_percent_votes), '.3%'))} ({len(TotalOTooley)})\n")

p.write("-----------------------------------\n")
p.write(f"Winner: {ElectionWinner}\n")

p.write("-----------------------------------\n")