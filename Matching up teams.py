from collections import deque

numberOfTeams = int(input("Enter the number of teams: "))

teamQueue = deque(range(1, numberOfTeams))

out = []

for i in range (0, numberOfTeams-1):
    """
    For the number of rounds we have.
    A round is a set of games where each team plays once only.
    The teams are then roated through a queue at the end of each round
    This then seeds the unique start for next round.
    """

    for x in range (1,numberOfTeams//2):
        #Goes through the queue paring teams up from either end
        out.append((teamQueue[x], teamQueue[numberOfTeams - x - 1]))

    #One team needs to stay 'stationary' in the queue
    out.insert((i*((numberOfTeams//2) + 1)), (teamQueue[0] , numberOfTeams))

    
    #Move everyone along and wrap the end    
    teamQueue.append(teamQueue[0])
    teamQueue.popleft()

    

for i in range (0, len(out)):
    print(out[i][0], " Vs ", out[i][1])

print(len(out))

