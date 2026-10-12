import pandas as pd
import datetime

data = pd.read_csv(r"C:\Users\XXXXXXX\Downloads\InventoryAllFields (52).csv")
#Change the number in paraenthesis to the actual file most recently downloaded

print(data["Status"].value_counts())
print(data["Category"].value_counts())
print(data["Aging (days)"].describe())
#DEBUG: This will tell us the values inside the columns

filtered_data = data[
    (data["Status"] == " **Released**") &
    (data["Category"] != "Monitors") &
    (data["Aging (days)"] >= 30)
    (data["Category"] != "Servers") &
    #This makes sure that the data must include all 3 of these filters. & allows us to do so. The () is important as each line is a special segment to itself
]

print("Total rows:", len(data))
print("Released:", len(data[data["Status"] == " **Released**"]))
print("Not Monitors:", len(data[data["Category"] != "Monitors"]))
print("Aging 30+:", len(data[data["Aging (days)"] >= 30]))
#DEBUG: This will tell us what survives our filter when we try to add them to the DF

sorted_data = filtered_data.sort_values(
    by="Aging (days)",
    ascending=False
    #after establishing the data set we filter through a column 'Aging Days' and have the filter start with the largest numbers
)
Today = pd.to_datetime('today').strftime('%Y-%m-%d')

sorted_data.to_excel(
    r"C:\Users\XXXXX\Documents\Excel Sheets\Days Aging" + str(Today) + ".xlsx",
    index=False
#lists the directory for the file to be stored, adds today's date to the file, then turn the file into xlsx
)

print(data.head(3))
print(data.tail(5))
print(data.columns)


#Issues 1, the excel sheet comes out blank but leaves the header of the columns in-place, no other data is populated.
#Solution: After using Debugging tool found out that after our filter was working the number of 'Released' units was 0 and therefore not populating what we wanted

#Issue 2, the Debugging print command said that the column for 'Released' was 0 meaning that was the source of the issue.
#Solution: When looking back at the data sheet for the original CSV, the column for state has 'Released' as " **Released**" when I was typing it as "**Released**".
#There was a space before the two ** that needed to be added. 