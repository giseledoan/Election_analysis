
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes. 
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#use datetime module to get today's date 
import datetime
now = datetime.datetime.now()
print("The time right now is", now)

#Open file by direct path
##Assign a variable for the file to load and the path.
file_to_load = 'C:\\Users\\trang doan\\OneDrive\\Desktop\\Analysis projects\\Election_analysis\\Resources\\election_results.csv'
##Open the election results and read the file.
with open(file_to_load) as election_data:
##To-do: Perform analysis.
    print(election_data)

#Print total votes, candidate's name & votes
##Add dependencies.
import csv
import os
##Assign a variable "file to load" for "election_result.csv" by indirect path.
file_to_load = os.path.join(".","Resources","election_results.csv")
##Assign a variable "file to save" to save output file (after creating analysis folder)
file_to_save = os.path.join("analysis", "election_analysis.txt")
##Create election_analysis.txt
with open(file_to_save,"w") as txt_file:
    ###Write some data to the txt.
    txt_file.write("Counties in the election\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")

##Initialize a total vote counter.
total_votes = 0
##Declare a new list "candidate_options" for candidate's name
candidate_options = []
##Declare a new dictionary "candidate_votes" for candidate's votes
candidate_votes = {}
##Declare variable to count winning candidate, winning count & winning %
winning_candidate = " "
winning_count = 0
winning_percentage = 0

##Open the "file to load" (election_results.csv) and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    ###Read the header row to skip it in votes count.
    headers = next(file_reader)
    ###Print each row in the CSV file.
    for row in file_reader: #(file_reader is csv file)
        #### Add to the total vote count.
        total_votes +=1 #variable increase by 1 when we read each row
        #### Print the candidate name from each row
        candidate_name = row [2]
        #### if candidate name has not been added to list, add it.
        if candidate_name not in candidate_options:
            ##### Add it to the list of candidate_options
            candidate_options.append(candidate_name)
            ##### Track that candidate's vote count, start w 0
            candidate_votes[candidate_name] = 0
        #### Add a vote to each candidate's count, increase 1 when we read each candidate name.
        candidate_votes[candidate_name] +=1
    ### Save the results to our text file.
with open(file_to_save, "w") as txt_file:
                #Print final vote count to the terminal
    election_results = (f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------\n")
    print(election_results, end="")
            #Save the final vote count to the text file.
    txt_file.write(election_results)

##Print the candidate vote dictionary (inclde name & votes)
    print(candidate_votes)


#Calculate percentage of votes
##Iterate through the candidate list dictionary to get their name:
    for candidate_name in candidate_votes:
    ### retrieve vote count of a candidate, can_name = row [2]
        votes = candidate_votes[candidate_name]
    ### calcuate percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100
#Print the candiate name, vote count & percentage of votes
        candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        #Determine if votes > winning count:
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true, set winning_count = votes and winning % = vote %
            winning_count = votes
            winning_percentage = vote_percentage
            #Set winning candidate = candidate name
            winning_candidate = candidate_name
    #Print out the winning candidate summary
    winning_candidate_summary = (f"------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote Count:{winning_count:,}\n"
    f"Winning Percentage:{winning_percentage:.1f}%\n"
    f"-------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's result to the txt file
    txt_file.write(winning_candidate_summary)
    