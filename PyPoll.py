# Data that needs to be retrieved - psuedocoding
# 1. Total number of votes cast
# 2. A complete list of candidates received 
# 3. Total number of votes each candidate received 
# 4. The winner of the election based on popular vote 

 # Assign a variable for the file to load and the path.
file_to_load = 'c:/Users/Justin Yen/Desktop/Utor/Module 3 - Python/Election_Analysis\Resources\election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

import csv
import os
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w") 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

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
    print(headers) 