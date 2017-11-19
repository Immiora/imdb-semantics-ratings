
files = ['1.txt',
'new_IDs_IDincrement_5000000_endID_9999999_12-00-00.txt',
'new_IDs_startyear_1950_endyear_1965_12-00-00.txt',
'new_IDs_startyear_1950_endyear_1980_12-00-00.txt',
'new_IDs_startyear_1980_endyear_1990_12-00-00.txt',
'new_IDs_startyear_2010_endyear_2020_12-00-00.txt',
'new_IDs_startyear_2010_endyear_2020_12-00-10.txt',
'new_IDs_startyear_1950_endyear_1980_12-00-100.txt',
'new_IDs_startyear_1980_endyear_1990_12-00-01.txt',
'new_IDs_startyear_2010_endyear_2020_12-00-11.txt',
'new_IDs.txt']

fullList = []
for fileName in files: 
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    for line in content:
        if (len(line) < 14 and line[0:2] == "tt"):
            fullList.append(line)
        for word in line.split():
            if (len(word) == 9):
                if (word[0:2] == "tt"):
                    fullList.append(word)
        
listAsSet = set(fullList)
uniqueList = list(listAsSet)

theFile = open('new_IDs_2.txt', 'w')
for id in uniqueList:
    theFile.write("%s\n" % id)
