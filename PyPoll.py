
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

#Open file w direct path
#Assign a variable for the file to load and the path.
file_to_load = 'C:\\Users\\trang doan\\OneDrive\\Desktop\\Analysis projects\\Election_analysis\\Resources\\election_results.csv'
#Open the election results and read the file.
with open(file_to_load) as election_data:
#To-do: Perform analysis.
    print(election_data)

#Open file w indirect path
#Add dependencies.
import csv
import os
#Assign a variable "file to load" for "election_result.csv" from a path.
file_to_load = os.path.join(".","Resources","election_results.csv")
#Assign a variable "file to save" to save output file (after creating analysis folder)
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the "file to load" (election_results.csv) and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here
    #Read "file to load" (election_result.csv as election_data) w the reader function
    file_reader = csv.reader(election_data)
    #Reade and print the header row.
    headers = next(file_reader)
    print(headers)