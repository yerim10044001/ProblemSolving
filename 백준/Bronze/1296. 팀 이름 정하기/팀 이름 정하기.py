def getProbability(name, teamName):
    l = name.count('L')+teamName.count('L')
    o = name.count('O')+teamName.count('O')
    v = name.count('V')+teamName.count('V')
    e = name.count('E')+teamName.count('E')

    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100

name = input()

n = int(input())

maxProbability = 0
maxTeamName = ""

for _ in range(0,n):
    teamName = input()
    nameCount = []

    probability = getProbability(name, teamName)
    
    if maxTeamName == "":
        maxTeamName = teamName
        maxProbability = probability

    # get max probability TeamName
    if probability >= maxProbability:
        # if maxProbability is equal, get teamName in alphabetic order
        if probability == maxProbability:
            if teamName<maxTeamName:
                maxTeamName = teamName
        else:
            maxProbability = probability
            maxTeamName = teamName

print(maxTeamName)