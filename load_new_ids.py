
files = ['new_IDs_start_151_end_244_12-00-00.txt',
'new_IDs_start_101_end_150_12-00-00.txt',
'new_IDs_start_51_end_100_12-00-00.txt',
'new_IDs_start_0_end_50_12-00-00.txt']

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

theFile = open('new_IDs.txt', 'w')
for id in uniqueList:
    theFile.write("%s\n" % id)
