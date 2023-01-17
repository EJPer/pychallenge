import csv
import os

file_path = os.path.join('..','Data_sets_for_examples', 'election_data.csv')
    
with open(file_path) as electioncsv:
    electiondata = csv.reader(electioncsv, delimiter = ',')
    
    header = next(electiondata)
    
    votecount = 0
    charles = 0
    diana = 0
    raymon = 0
    
    for rows in electiondata:
        votecount += 1
    
        if rows[2] == "Raymon Anthony Doane" :
            raymon += 1
        
        elif rows[2] == "Diana DeGette":
            diana += 1
        
        elif rows[2] == "Charles Casper Stockham":
            charles += 1
        
    
    percentcharles = round((charles / votecount)*100, 3) 
    percentdiana = round((diana / votecount)*100, 3)
    percentraymon = round((raymon / votecount)*100,3)
    
    winner = max(charles, diana, raymon)
    
    print("Election Results")
    print("----------------")
    print(votecount)
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