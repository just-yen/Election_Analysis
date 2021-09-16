# Election_Analysis

## Overview

### Purpose 
The purpose of the election audit is to provide the requested data points from the election commission. The audit will provide data points regarding voter turnout for each county, the percentage of votes from each county out of the total count, the county with the highest turnout. In addition, data points regarding candidate's vote percentage and vote count are included in the audit. 

### Tools and Resources
Script used to to retreive data points for the election comission were based off a previous script used to collect candidate data. The original script can be found here [PyPoll](https://github.com/just-yen/Election_Analysis/blob/master/PyPoll.py).
Python, git bash, and CSV files were additional resources used. 

## Election-Audit Results:

![Election-Audit Results](https://github.com/just-yen/Election_Analysis/blob/master/analysis/election_analysis%20png.PNG)


- How many votes were in the congressional election? 

  There was 369,711 total votes.

- Breakdown of the number of votes and percentage of total votes for each county

  Jefferson: 10.5% (38,855),
   Denver: 82.8% (306,055),
    Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes?

  Denver: 82.8% (306,055)

- Number of votes and the percentage of the total votes each candidate received 

  Charles Casper Stockham: 23.0% (85,213),
  Diana DeGette: 73.8% (272,892),
  Raymon Anthony Doane: 3.1% (11,606)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
 
  Diana DeGette won the election, with 272,892 votes and 73.8% percentage of total votes. 

## Election-Audit Summary 

### Conclusion
The scipt itself has proven effective in producing accurate and presentable results. There is room for potential refactoring especially in relation to combining the for loop codes and dictionary lists. So far, the script remains effective however, there may be causes for concerns when additional lists and categories are required to be used to answer queries.  

### Business proposal 
The script remains flexible and can be used with modifications for any elections. Below are my two proposals for modified uses regarding the upcomming 2021 Canada Federal Election. 

1. Fact Checking 
I believe the script can be modified to include a statistical breakdown of how many times each Canada party leader has made false claims, truth stretches, and correct claims. With a CSV file providing the data points, the script can be modified to retreive and calculate the count and % breakdown the same way it does for county total counts and percentage %. 

3. Federal Election Vote Gains/Loss 
The script can be modified to provide historical data comparisons as well. The script would import two CSV files and modified to perform two separate calculations for comparison points. The purpose would be to provide a canddiate name, total count, and percentage breakdown for any political parties running in the federal elections. 
