predata = []
buffer = []
postdata = []
word=''
database = []
keep = []

file = open("./lc_commandItems.h","r")
data = file.readlines()
for i in data:
        if "QObject::tr" in i:
            k = i.split(',')
            predata.append(k)
file.close()
for i in range(len(predata)):#Grouped lines
    for k in range(len(predata[i])):#Individual lines
        for j in range(len(predata[i][k])):#Individual words
            for x in range(len(predata[i][k][j])):#Individual Character
                if predata[i][k][j][x].isalnum():
                    word += predata[i][k][j][x]
        buffer.append(word)
        word = ''
    #So by my interpretation of data all tools almost look like:                                                
    #[toolname,sometranslationdata,description,'nullchar'] so 4 
    if len(buffer) == 4 and not 'QObjecttr' in buffer[0] and not buffer[2]=='translationText':
        postdata.append(buffer)
    buffer = []
#print(predata)
#print(postdata)

#group the tools as per their descriptions[[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]...]
alias = []
count = 0
flag = True

for i in range(len(postdata)): #iterate through records
    for k in range(i+1,len(postdata)): #iterate in next record
            if postdata[i][2]== postdata[k][2]:
                for z in database:
                    if postdata[k][2] in z[2]:
                        flag = False
                        #flag2 = False
                if flag == True:
                    alias.append(postdata[k][0])                                                                  
                flag = True

    database.append([postdata[i][0],alias,postdata[i][2]])   
    alias = []
#print(database)
for i in database:
    if not i[1] == []:
        keep.append(i)
print(keep)
#first file data is over 
#filec = open('HT.txt','r')
#datac = filec.read()
#predatac = 
#print(datac)

#okay now i won't change anything above just need to format it , that's it, one binary and one csv or md file and add the data by running another file.

import csv
FD = open("./Data.csv",'w')
writer = csv.writer(FD)
writer.writerows(keep)
