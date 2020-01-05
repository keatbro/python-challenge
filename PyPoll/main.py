# Import Dependencies
import csv
import os

# Set initial variable values
total_votes = 0
candidates = []
voteCount = {}
votePercent = []

# Set File Path
csvpath = os.path.join('Resources', 'election_data.csv')

# Open CSV
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    csvreader = list(csvreader)

    # Iterate through rows in CSV
    for row in csvreader:

        # Count all votes
        total_votes += 1

        # Get list of distinct candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        # Add votes counts to dictionary
        candidate = row[2]
        
        # If candidate isn't already in vote dictionary, add them and give them one vote, else add a vote.
        if candidate not in voteCount:
            voteCount[candidate] = 1
        else: 
            voteCount[candidate] +=1

        # Copy voteCount dictionary values into their own list so you can reference them in the same output format.
        voteCountList = list(voteCount.values())

    # Get vote percentages from dictionary, format, and add them to list.
    for person in voteCount:
        percentage = (voteCount[person] / total_votes) * 100
        percentage = '%.3f%%' % percentage
        votePercent.append(percentage)

    # Get max votes from voteCount dictionary
    winner = max(voteCount, key=lambda k:voteCount[k])

# Make function to print out info per candidate
def listInfo():
    for name in range(len(candidates)):
        print(f"{candidates[name]}: {votePercent[name]} ({voteCountList[name]})")

# Print results to terminal
stats = (
    f'Election Results \n'
    f'------------------- \n'
    f'Total Votes: {total_votes} \n'
    f'------------------- \n'
)
print(stats)

listInfo()

stats2 = (
    f'------------------- \n'
    f'Winner: {winner}'
)
print(stats2)

# Export printed results to a text file
textFile = os.path.join('text.txt')
with open (textFile, 'w') as myFile:
    writer = myFile.write(stats)
    
    for name in range(len(candidates)):
        lines = (f'{candidates[name]}: {(votePercent[name])} ({(voteCountList[name])})')
        myFile.write('{}\n'.format(lines))
    writer = myFile.write(stats2)