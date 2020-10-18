import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

months = 0
net_total = 0
greatestincrease = 0
greatestdecrease = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")

    next(csvreader)

    for row in csvreader:
        months = months+1
        # net_total = net_total + row[2]


print(f"Total Months: {months}")
print(f"Total: {net_total}")
averagechange = net_total/months
print(f"Average Change: {averagechange}")

print(f"Greatest Increase in Profits: {greatestincrease}")
print(f"Greatest Decrease in Profits: {greatestdecrease}")


# output_file = os.path.join("analysis", "analysis.txt")
# with open(csvpath) as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(['Date', 'Profit'])
        
