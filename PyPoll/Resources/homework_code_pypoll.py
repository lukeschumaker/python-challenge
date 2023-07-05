import os
import csv
csvpath = os.path.join('..','python-challenge','PyPoll/Resources','election_data.csv')

#Create an empty dictionary to hold the candidates and their votes.
candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #Read each row of data after the header

    total_votes = 0
    
    for row in csvreader:

        total_votes += 1
        #If the candidate is already in the dictionary, increment the count else
        #add the candidate's name to the dictionary

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    
print ('Election Results')
print('-------------------')
print(f'\nTotal Votes: {total_votes}')
print('-------------------')

most_votes = 0
most_votes_candidate = ''
for key, value in candidates.items():
    print(f'{key}: {round(value/total_votes*100,3)}% ({value} votes)')
      
    if value > most_votes:
        most_votes = value
        most_votes_candidate = key
print('-------------------')
print(f'\nWinner: {most_votes_candidate}')
print('-------------------')

#Reference text file with the intention of writing to it.
pypoll_output = open("pypoll_output.txt", "w")

pypoll_output.write('Election Results')
pypoll_output.write('\n------------------------')
pypoll_output.write('\n Total Votes:')
pypoll_output.write(f'{total_votes}')
pypoll_output.write('\n------------------------')

for key, value in candidates.items():
    pypoll_output.write(f'\n{key}:')
    pypoll_output.write(f'{round(value/total_votes*100,3)}% ({value} votes)')

pypoll_output.write('\n------------------------')
pypoll_output.write(f'\nWinner: {most_votes_candidate}')
pypoll_output.write('\n------------------------')
pypoll_output.close()


        
