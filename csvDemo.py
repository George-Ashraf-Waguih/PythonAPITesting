import csv
from os import write

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    # print(list(csvReader))
    # print('------------------')
    names=[]
    stats=[]

    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

Index = names.index('Joe')
print(Index)
loanStatus = stats[Index]
print(f'Joe loan status is {loanStatus}')

# with open('utilities/loanapp.csv','w') as csvFile:   Using w will write the file from beginning and delete already written before

with open('utilities/loanapp.csv','a') as wFile:
    write = csv.writer(wFile)
    write.writerow(['Bob1','rejected'])
    write.writerow(['Bob2', 'rejected'])