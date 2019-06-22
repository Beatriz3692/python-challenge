# Dependencies 
import os
import csv 

# find path
election_data = os.path.join("election_data.csv")

# create empty lists
candidate = []
vote_count = 0
Khan_votes = 0 
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

# open and read csv
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # go through each row
    for row in csvreader:
        
        # append total number of votes
        candidate.append(row[2])

        if row[2] == "Khan":
            Khan_votes +=1
        elif row [2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            Otooley_votes += 1

# list candidates
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [Khan_votes, Correy_votes, Li_votes, Otooley_votes]

# count votes
vote_count = len(candidate)

# percentage
Khan_per = Khan_votes/vote_count*100
Correy_per = Correy_votes/vote_count*100
Li_per = Li_votes/vote_count*100
Otooley_per  = Otooley_votes/vote_count*100

# percentage list
per_list = [Khan_per, Correy_per, Li_per, Otooley_per]

winner = ''
winnercount = 0 

for x in range(0, len(per_list)):
    if per_list[x] > winnercount:
        winnercount = per_list[x]
        winner = candidates[x]

output = "Election Results" + "\n" + "-------------------------" + "\n" + "Total Votes: " + str(vote_count) + "\n" + "-------------------------" + "\n" + "Khan: " + str(Khan_per) + "%" + "\n" "Correy: " + str(Correy_votes) + "%" + "\n" + "O'Tooley: " + str(Otooley_per) + "%" + "\n" + "-------------------------" + "\n" + "Winner: " + str(winner) + "\n" + "-------------------------" 

print(output)
