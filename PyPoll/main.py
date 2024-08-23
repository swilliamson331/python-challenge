import os
import csv

bank_csv = os.path.join("Resources", "election_data.csv")

#read file
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skip header
    next(csv_file)
    # Define variables
    total_votes = 0
    candidates = []
    votes = {}

     #loop through rows
    for row in csv_reader:
        #number of votes in dataset
        total_votes += 1
        # candidates column
        candidates = str(row[2])
        # number of votes per candidate
        if candidates not in votes:
            votes[candidates] = 1
        else:
            votes[candidates] += 1

#print total votes
print(f"""Election Results
----------------------------
Total votes: {total_votes}
----------------------------\n""")

#calculate percentages of vote totals while looping through the rows
for candidates, votes in votes.items():
    percent = round((votes / total_votes) * 100, 3)
    # print the candidates with their vote percentages and totals
    print(f"{candidates}:  {percent}%  ({votes})\n")

#print the winner
print(f""" ----------------------------
Winner: Diana DeGette
----------------------------""")

# Export analysis results to a txt file using the terminal command python main.py | tee Analysis/analysis.txt
