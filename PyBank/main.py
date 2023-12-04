# import modules
import os
import csv

#file path
csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
prof_loss = []
with open(csvpath) as csvfile:

    #specify delimiter and variable to hold csv data
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header
    csv_header = next(csvreader)

    # Read each row and store values in arrays
    for row in csvreader:
        months.append(row[0])
        prof_loss.append(int(row[1]))

# variable to hold greatest increase and greatest decrease in profits and their indexes
max_inc = 0
max_inc_index = 0
max_dec = 0
max_dec_index = 0

# array to hold all changes between months
total_change = [] 
# loop through the data to find the greates increase and the greatest decrease
for i in range(len(months)-1):
    if(prof_loss[i+1]-prof_loss[i]>max_inc):
        max_inc = (prof_loss[i+1]-prof_loss[i])
        max_inc_index = i+1
    if(prof_loss[i+1]-prof_loss[i]<max_dec):
        max_dec = (prof_loss[i+1]-prof_loss[i])
    # add the change of the iteration to the array
    total_change.append(prof_loss[i+1]-prof_loss[i])

#print results
print("\nFinancial Analysis") 
print("--------------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(sum(prof_loss)))
print("Average Change: $" + str(round(sum(total_change)/len(total_change),2)))
print("Greatest Increase in Profits: " + months[max_inc_index] + " ($" + str(max_inc) + ")")
print("Greatest Decrease in Profits: " + months[max_dec_index] + " ($" + str(max_dec) + ")\n")

#write results to text file
f = open("analysis\PyBank_results.txt","w")
f.write("Financial Analysis\n") 
f.write("--------------------------------\n")
f.write("Total Months: " + str(len(months)) + "\n")
f.write("Total: $" + str(sum(prof_loss)) + "\n")
f.write("Average Change: $" + str(round(sum(total_change)/len(total_change),2)) + "\n")
f.write("Greatest Increase in Profits: " + months[max_inc_index] + " ($" + str(max_inc) + ")\n")
f.write("Greatest Decrease in Profits: " + months[max_dec_index] + " ($" + str(max_dec) + ")\n")
f.close()