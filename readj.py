
import json
import csv
jsonlist=['aapl-summary.json','msft-summary.json','tgt-summary.json']

array1=[]
array1.append([])

with open (jsonlist[1]) as jname:
    namels = json.load(jname)
    nameval=list(namels.keys())
for index in range(18):
    array1[0].append(nameval[index])



for i in range(3):
    with open (jsonlist[i]) as jj:
        data = json.load(jj)
        values=data.values()
        l=list(values)
        array1.append([])
        for j in range(18):
            array1[i+1].append(l[j])



print(array1)

with open("stockdata.csv","w",newline='')as mycsv:
    csvWriters=csv.writer(mycsv,delimiter=',')
    csvWriters.writerows(array1)



