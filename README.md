This project is meant to take several parts of my day and automate the reports that I have to gather at the end of each work day.

Part 1 *Completed/Working*
The first script PV_Excel is meant to login to the website we use, find the where we story our inventory database, put certain key filter words into the filters, then pull up the correct inventory based on those filters.
Once the correct inventory has been spotted it will download the report into an excel document.

Part 2 *Completed*
I will take the document it downloads and organize the data into a table with certain filters.
This excel code will be focused on organizing our data based off of oldest entry and will focus on only showing inventory or 30 days from the time it arrives to our facility.

10/12/26
-I was able to take the csv load it with pandas and filter the data that I need. The report pulls the entire inventory of the facility so I narrow it down to ignore a few things.  I have a few lines of degugging code in there to make sure the filters arent getting rid of the data I need. On top of that it is to also show how many lines of information will be presented at the very end of the filters running.

Part 3 *Completed*
This code is very similar to part 1 where I just need to pull a report from the website. Very similar format and style, but instead of filling in filters on the website to pull a CSV this report just needs to be selected after after navigating to the right webpage. 


Part 4 *WIP*
This is where I will take The report from part 3 and turn it into a 2 pivot tables in excel. It will take the information from one of the sheets in excel and transcribe it into two pivot tables. 1st pivot table will show employee names and how much production done in a day and the 2nd one will show how much production was done each hour.

To be continued
Part 5
