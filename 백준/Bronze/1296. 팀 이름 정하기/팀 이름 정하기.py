def getProbability(name, teamName):
    l = name.count('L')+teamName.count('L')
    o = name.count('O')+teamName.count('O')
    v = name.count('V')+teamName.count('V')
    e = name.count('E')+teamName.count('E')

    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100

def setMaxProbabilityTeam(probability, teamName):
    global maxProbability
    global maxTeamName
    if probability > maxProbability:
        maxProbability = probability
        maxTeamName = teamName
    # if maxProbability is equal, get teamName in alphabetic order
    elif probability == maxProbability and teamName<maxTeamName:
        maxTeamName = teamName


if __name__ == "__main__":
    name = input()
    n = int(input())
    maxProbability = 0
    maxTeamName = ""

    for _ in range(0,n):
        teamName = input()
        nameCount = []

        probability = getProbability(name, teamName)

        # set init teamName
        if maxTeamName == "":
            maxTeamName = teamName
            maxProbability = probability
            continue

        # get max probability TeamName
        setMaxProbabilityTeam(probability, teamName)

    print(maxTeamName)