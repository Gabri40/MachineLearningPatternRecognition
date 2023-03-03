#open file and read to list of strings
with open("/home/gabri/Polito/ii - Magistrale/0-repos/MachineLearningPatternRecognition/lab1/score.txt") as inputfile:
    filecontent=inputfile.readlines()

#split each string in the list to a list of strings
fields=map(lambda s:s.split(" "),filecontent)

#list of [player_n player_s country score ...]
playerscores=list(fields)
ps=[]
cs=[]

for player in playerscores:
    name=player[0]+" "+player[1]
    country=player[2]

    maxi=0
    mini=200
    for i in range(3,8):
        tmp=float(player[i])
        if tmp>maxi: maxi=i
        if tmp<=mini: mini=i
        else: player[i]=tmp
    player[maxi]=0.0
    player[mini]=0.0

    score=0
    for i in range(3,8): score+=player[i]

    ps.append([name,score])
    cs.append([country,score])


print()
print("podium:")
ps.sort(key=lambda x:x[1],reverse=True)
for player in ps[:3]: 
    print(player[0]+": "+str(player[1]))


print()
print("best country:")
for cstuple in cs:
    for cstuple2 in cs:
        if cstuple[0]==cstuple2[0] and cstuple[1]!=cstuple2[1]:
            cstuple[1]+=cstuple2[1]
            cstuple2[1]=0.0
cs.sort(key=lambda x:x[1],reverse=True)
print(cs[0][0]+": "+str(cs[0][1]))
print()


