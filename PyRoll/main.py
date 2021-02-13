import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

Votecount = 0
Kcount = 0
Ccount = 0
Lcount = 0
Ocount = 0
candidate = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip header
    
    for row in csvreader:
        
       # Checks for unique list of candidates
        if row[2] not in candidate:
            candidate.append(row[2])
        
        Votecount = Votecount+1 
        
        #Count number of votes per candidate using a counter for each candidate
        if row[2] == "Khan":
            Kcount = Kcount+1
        elif row[2] == "Correy":
            Ccount = Ccount+1
        elif row[2] == "Li":
            Lcount = Lcount+1
        elif row[2] == "O'Tooley":
            Ocount = Ocount+1
        
    #Percent of votes per candidate    
    Kperc = round(100*Kcount/Votecount,3)
    Cperc = round(100*Ccount/Votecount,3)
    Lperc = round(100*Lcount/Votecount,3)
    Operc = round(100*Ocount/Votecount,3)
    
    CandCount = [Kcount, Ccount, Lcount, Ocount]
    Perclist = [Kperc,Cperc,Lperc,Operc]
    
    #Check winner using max
    if max(Perclist) == Kperc:
        Winner = "Khan"
    elif max(Perclist) == Cperc:
        Winner = "Correy"
    elif max(Perclist) == Lperc:
        Winner = "Li"
    elif max(Perclist) == Operc:
        Winner = "O'tooley"
    

Election_results = {"Total Votes": Votecount,
                    "Candidates" : candidate,
                    "Percent Votes": Perclist,
                    "Candidate Votes": CandCount,
                    "Winner" : Winner
                    }
print(f'Election Result\n ------------------')
print(f'Total Votes: {Election_results["Total Votes"]}\n------------------')
for x in range(len(candidate)):
    print(f'{Election_results["Candidates"][x]}: {Election_results["Percent Votes"][x]}% ({Election_results["Candidate Votes"][x]})')
print(f'------------------')
print(f'Winner: {Election_results["Winner"]} Congratulations!')
    
output_file = os.path.join("analysis", "Election_Analysis.txt")

with open(output_file, "w") as txtfile:
    txtfile.writelines(f'Election Result\n------------------\n')
    txtfile.writelines(f'Total Votes: {Election_results["Total Votes"]}\n------------------\n')
    for x in range(len(candidate)):
        txtfile.writelines(f'{Election_results["Candidates"][x]}: {Election_results["Percent Votes"][x]} ({Election_results["Candidate Votes"][x]}) \n')
    txtfile.writelines(f'------------------\n')
    txtfile.writelines(f'Winner: {Election_results["Winner"]}, Congratulations!')