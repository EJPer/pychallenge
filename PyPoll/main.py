# import packages
import csv
import os

#Read in Data
file_path = os.path.join('PyPoll','Resources','election_data.csv')

    
with open(file_path) as electioncsv:
    electiondata = csv.reader(electioncsv, delimiter = ',')
    
#set variables before for loop
    header = next(electiondata)
    
    votecount = 0
    charles = 0
    diana = 0
    raymon = 0
    
#For loop to find variables
    for rows in electiondata:
        votecount += 1
    
        if rows[2] == "Raymon Anthony Doane" :
            raymon += 1
        
        elif rows[2] == "Diana DeGette":
            diana += 1
        
        elif rows[2] == "Charles Casper Stockham":
            charles += 1
        
#calculating results after loop  
    percentcharles = round((charles / votecount)*100, 3) 
    percentdiana = round((diana / votecount)*100, 3)
    percentraymon = round((raymon / votecount)*100,3)
    
    winner = max(charles, diana, raymon)

#Results
    print("Election Results")
    print("----------------")
    print(f"Total Votes Cast: {votecount}")
    print("-----------------")
    print(f"Charles Casper Stockham: {charles} ({percentcharles})%")
    print(f"Diana DeGette: {diana} ({percentdiana})%")
    print(f"Raymon Anthony Doane: {raymon} ({percentraymon})%")
    
    print("----------------")
    
    if winner == charles:
        print("Winner: Charles Casper Stockham")
    elif winner == diana:
        print("Winner: Diana DeGette")
    elif winner == raymon:
        print("Winner: Raymon Anthony Doane")

with open("Pypolls.txt", "a") as pypolls:
    print("Election Results", file=pypolls)
    print("----------------", file=pypolls)
    print(f"Total Votes Cast: {votecount}",file=pypolls)
    print("-----------------",file = pypolls)
    print(f"Charles Casper Stockham: {charles} ({percentcharles})%",file=pypolls)
    print(f"Diana DeGette: {diana} ({percentdiana})%", file=pypolls)
    print(f"Raymon Anthony Doane: {raymon} ({percentraymon})%", file=pypolls)
    print("----------------",file = pypolls)
    
    if winner == charles:
        print("Winner: Charles Casper Stockham", file = pypolls)
    elif winner == diana:
        print("Winner: Diana DeGette",file=pypolls)
    elif winner == raymon:
        print("Winner: Raymon Anthony Doane",file=pypolls)