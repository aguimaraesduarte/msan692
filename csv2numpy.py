import numpy as np
import sys
import csv

table_file = sys.argv[1]
with open(table_file, "rb") as csvfile:
    f = csv.reader(csvfile, dialect='excel')
    data = []
    for row in f:
    	if row != []:
	        data.append(row)

data = np.array(data)
#print data

#order quantity = row[4]
#unit price = row[9]

saleValue = [float(entry[4])*float(entry[9]) for entry in data[1:]]
saleValue = np.array(saleValue)

#orderQuantity = [float(entry[4]) for entry in data[1:]]
#unitPrice = [float(entry[9]) for entry in data[1:]]
#saleValue = np.multiply(orderQuantity, unitPrice)

print saleValue
