
files = ['new_IDs_startyear_2001_endyear_2010_12-00-00.txt',
'new_IDs_startyear_1990_endyear_2000_12-00-00.txt',
'new_IDs_startyear_1980_endyear_1990_12-00-00.txt',
'new_IDs_startyear_2010_endyear_2020_12-00-00.txt',
'new_IDs.txt']

fullList = []
for fileName in files: 
    with open(fileName) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    for line in content:
        if (len(line) < 14 and line[0:2] == "tt"):
            fullList.append(line)
        
listAsSet = set(fullList)
uniqueList = list(listAsSet)

theFile = open('new_IDs_2.txt', 'w')
for id in uniqueList:
    theFile.write("%s\n" % id)
