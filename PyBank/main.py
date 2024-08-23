import os
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")

#read file
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skip header
    next(csv_file)
    #define variables
    total_months = 0
    profits_losses = 0
    p_l_column = []
    biggest_increase = None
    biggest_decrease = None
    increase_date = None
    decrease_date = None
    #loop through rows
    for row in csv_reader:
        #number of months in dataset
        total_months += 1
        #total profits/losses
        profits_losses += int(row[1])
        #column read for average p/l change
        p_l_column.append(int(row[1]))
        # biggest increase and decrease
        if len(p_l_column) > 1:
            changes = p_l_column[-1] - p_l_column[-2]
            if biggest_increase is None or changes > biggest_increase:
                biggest_increase = changes
                increase_date = row[0]
            if biggest_decrease is None or changes < biggest_decrease:
                biggest_decrease = changes
                decrease_date = row[0]

#calculate average change
change = [p_l_column[i] - p_l_column[i-1] for i in range(1, len(p_l_column))]
average = round((sum(change) / len(change)), 2)

# old biggest and smallest changes before I realized I couldn't get date with this method
# increase = max(change)
# decrease = min(change)

#print results to terminal
print(f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${profits_losses}
Average Change: ${average}
Greatest Increase in Profits: {increase_date} (${biggest_increase})
Greatest Decrease in Profits: {decrease_date} (${biggest_decrease})""")

# Exporting analysis results to a txt file
Analysis = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${profits_losses}
Average Change: ${average}
Greatest Increase in Profits: {increase_date} (${biggest_increase})
Greatest Decrease in Profits: {decrease_date} (${biggest_decrease})"""

with open(os.path.join("analysis", "analysis.txt"), "w") as file:
    file.write(Analysis)
