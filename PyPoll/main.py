# import modules
import os
import csv

# function to calculate percent of one value to whole 
def percent(num,len):
    percent = num/len*100
    return str(round(percent,3))

# function to return number of occurences of an element in a list
def cand_count(cand, cand_list):
    return str(cand.count(cand_list))

# function to return individual candidate results
def print_results(cand_list,cand_votes,length):
    return(cand_list + ": " + percent(int(cand_votes),int(length)) + "% (" + str(cand_votes) + ")\n")
#file path
csvpath = os.path.join('Resources', 'election_data.csv')

# store data from csv file
ballot_id = [] # each unique vote
county = [] # home county of voters
candidate = [] # candidate that was voted for

# array of candidates who recieved votes and number of votes
cand_list = [] # list to hold each unique candidate
cand_votes = [] # list to hold number of votes each candidate received

with open(csvpath) as csvfile:

    # specify delimiter and variable to hold csv data
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header
    csv_header = next(csvreader)

    # Read each row and store values in arrays
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        if row[2] not in cand_list:
            cand_list.append(row[2])

#make array of number of votes per unique candidate
for j in range(len(cand_list)):
    cand_votes.append(int(cand_count(candidate,cand_list[j])))

#print results and write results to text file
print("\nElection Results")
print("-----------------------------")
print("Total Votes: " + str(len(ballot_id)))
print("-----------------------------")
# loop through each unique candidate and return their data
for j in range(len(cand_list)):
    #print(cand_list[j] + ": " + percent(int(cand_votes[j]),len(ballot_id)) + "% (" + str(cand_votes[j]) + ")")
    print(print_results(cand_list[j],cand_votes[j],len(ballot_id)))
print("-----------------------------")
# print candidate with maximum number of votes
print("Winner: " + str(cand_list[cand_votes.index(max(cand_votes))]))
print("-----------------------------\n")

#write results to text file
f = open("analysis\PyPoll_results.txt","w")
f.write("Election Results\n")
f.write("-----------------------------\n")
f.write("Total Votes: " + str(len(ballot_id)) + "\n")
f.write("-----------------------------\n")
# loop through each unique candidate and return their data
for j in range(len(cand_list)):
    f.write(print_results(cand_list[j],cand_votes[j],len(ballot_id)))
f.write("-----------------------------\n")
# print candidate with maximum number of votes
f.write("Winner: " + str(cand_list[cand_votes.index(max(cand_votes))])+ "\n")
f.write("-----------------------------\n")
f.close()