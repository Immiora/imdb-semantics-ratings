import pandas as pd


ids = []
actors1 = []
actors2 = []
actors3 = []

actorSet = set()

kaggleDbPath = 'kaggle_attr6.csv'
with open(kaggleDbPath) as f:
    content = f.readlines()
content = [x.strip('\n') for x in content]
for line in content[1:]:
    splitLine = line.split(';')
    id = splitLine[1]
    actorArrayStr = splitLine[4]
    if (len(actorArrayStr) != 0):
        actorArrayStr = actorArrayStr.replace('[', '').replace(']', '').replace('"', '').replace('\'', '')
        actors = actorArrayStr.split(', ')
        ids.append(id)
        actors1.append(actors[0])
        actors2.append(actors[1])
        actors3.append(actors[2])
        for actor in actors:
            actorSet.add(actor)

# actorList = list(actorSet)
dataFrame = pd.DataFrame({'id': ids, 'ACTOR1': actors1, 'ACTOR2': actors2, 'ACTOR3': actors3})
dummies = pd.get_dummies(dataFrame['ACTOR1'], columns=list(actorSet))
print('dummies: ' + str(len(dummies.columns)))
print('actors: ' + str(len(actorSet)))
        




