# Data that needs to be retrieved - psuedocoding
# 1. Total number of votes cast
# 2. A complete list of candidates received 
# 3. Total number of votes each candidate received 
# 4. The winner of the election based on popular vote 

 # Assign a variable for the file to load and the path.
# file_to_load = 'c:/Users/Justin Yen/Desktop/Utor/Module 3 - Python/Election_Analysis\Resources\election_results.csv'

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()

# import csv
# import os
# Open the election results and read the file
# with open(file_to_load) as election_data:

     # To do: perform analysis.
     # print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w") 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counte r
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.  

    # Read the file object with the reader function.
    # file_reader is referencing the file object, which is stored in memory.
    # To pull the data out of the file object, we can iterate through file_reader to print each row, including headers or column names 
    file_reader = csv.reader(election_data) 

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
     
     # To print first item from each row 
     # for row in file_reader:
          #print(row[0])
     
  # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    # next() method, add the variable file_reader that is referencing the file object assigned to the CSV file:
    # next(file_reader) will skip the first instance of what is being read. 
    headers = next(file_reader)

     # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)

# Add our dependcies for candidate name
import csv
import os 

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options. [] indicate new index/list
candidate_options = [] 

# Open the election results and read the file.
with open(file_to_load) as election_data: 
     file_reader = csv.reader(election_data)

     # Read the header row 
     headers = next(file_reader)

     # Print each row i nthe CSV file. 
     for row in file_reader:

          # Add to the total vote count. 
          total_votes += 1

          # Print the candidate name from each row. 
          candidate_name = row[2]

          # If the candidate does not match any existing candidate..
          if candidate_name not in candidate_options: 

          # Add the candidate name to the candidate list.
               candidate_options.append(candidate_name) 
     
     # Print the candidate list.
     print(candidate_options) 

# Add our dependencies for Candidate votes 

import csv
import os 

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0 

# Candidate options and candidate votes 
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Determine the winning candidate 
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data: 
     file_reader = csv.reader(election_data)

     # Read the header row
     header = next(file_reader)

     # Print each row in the CSV file
     for row in file_reader:
          
          # Add to the total vote count 
          # Python format to increment a variable is number = number + 1, which can be augmented to number += 1

          total_votes += 1 

          # Print the candidate name from each row 
          candidate_name = row[2]

          if candidate_name not in candidate_options: 

               # Add candidate name to the candidate's list 
               candidate_options.append(candidate_name)

               # 2. Begin tracking that candidate's vote count. 
               # we're setting each candidate's vote count to zero. Once we set it to zero, then we can start tallying the votes for each candidate.
               candidate_votes[candidate_name] = 0 

          # Add a vote to the candidate's count.
          # To increment each candidate's vote count every time their name appears in a row, we need to move the vote counter inside the for loop and have it align with the if statement.
          candidate_votes[candidate_name] += 1
     
     # Print the candidate vote dictionary
     print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.

# 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
    
    # 2. Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
    
    # 3. Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100
     
     # To do: print out each candidate's name, vote count, and percentage of
     # votes to the terminal.
          print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

     # Determine if the votes are greater than the winning count 
          if (votes > winning_count) and (vote_percentage > winning_percentage): 

     # 4. If true then set winning_count = votes and winning_percent = 
     # vote percentage 

               winning_count = votes 
               winning_percentage = vote_percentage

    # 5. Set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name 
    
    # 6. Print the candidate name and percentage of votes.

     # 7. To print out winning candidate summary
     winning_candidate_summary = (
         f"-------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"-------------------------\n")
print(winning_candidate_summary)





