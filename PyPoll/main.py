# Import the os module and module for reading CSV files
import os
import csv

# Path for the csv file
Election_Data = os.path.join('Resources','election_data.csv')

# Variable initialisation
Voter_Count = 0
Total_votes_cast = 0

# Lists to store Data
Voter_ID = []
County = []
Candidates = []
vote_Count =[]
Total_Vote_Per_Condidate = []
Percentage_votes = []


# Open the CSV
with open(Election_Data, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csv_reader)
    
    for row in csv_reader:
        
        Voter_ID.append (row[0])
        vote_Count.append (row[2])

        #The total number of votes cast
        Total_votes_cast= len (Voter_ID)
        ##print(Total_votes_cast)

    for i in set(vote_Count):
        Candidates.append(i)

        j= vote_Count.count(i)
        Total_Vote_Per_Condidate.append(j)

        k=round((j/Total_votes_cast)*100, 4)
        Percentage_votes.append(k)
       
    Winner = max (Total_Vote_Per_Condidate)    
   

#Print the election results to the terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+ str(Total_votes_cast))
    print("-------------------------")
    for a in range(len(Candidates)):
                print(Candidates[a] + ": " + str(Percentage_votes[a]) + "%  (" + str(Total_Vote_Per_Condidate[a]) + ")" )
    print("-------------------------")
    print("Winner: "+ str(Candidates[Total_Vote_Per_Condidate.index(Winner)]))
    print("-------------------------")

#Export a text file with the results
with open('Election Results', 'w') as textfile:
    print("Election Results", file=textfile)
    print("-------------------------", file=textfile)
    print("Total Votes: "+ str(Total_votes_cast), file=textfile)
    print("-------------------------", file=textfile)
    for a in range(len(Candidates)):
        print(Candidates[a] + ": " + str(Percentage_votes[a]) + "%  (" + str(Total_Vote_Per_Condidate[a]) + ")" , file=textfile)
    print("-------------------------", file=textfile)
    print("Winner: "+ str(Candidates[Total_Vote_Per_Condidate.index(Winner)]), file=textfile)
    print("-------------------------", file=textfile)