import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    next(csvreader)

    for row in csvreader:
        total_votes += 1

        if candidates.get(row[2]):
            candidates[row[2]] +=1
            
        else:
            candidates[row[2]]=1

print("----------------")
print("Election Results")
print("----------------")
print(f"Total votes: {total_votes}")
print("----------------")
# print(candidates)
# print(candidates.keys())

winning_vote=0
winning_candidate=""

for candidate_name, votes in candidates.items():
   # print(candidate_name)
   # print(votes)
    percentage = (votes/total_votes)*100
    percentagerounded = round(percentage,5)
   # print(f"{percentage}%")
    print(f"{candidate_name}:  {percentagerounded}%  {votes}")

    if votes > winning_vote:
        winning_vote = votes
        winning_candidate=candidate_name

print("----------------")
print(f"{winning_candidate} is the winning candidate")
print(f"{winning_vote} was the total vote count for {winning_candidate}")
print("----------------")


# printing to results.txt file
output_file = os.path.join("analysis", "analysis.txt")

with open(output_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([candidates])
    csvwriter.writerow([winning_candidate])
