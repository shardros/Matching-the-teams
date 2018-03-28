from collections import deque

numberOfTeams = int(input("Enter the number of teams: "))

teamQueue = deque(range(1, numberOfTeams))

out = []

for i in range (0, numberOfTeams-1):

    for x in range (1,numberOfTeams//2):
        out.append([teamQueue[x], teamQueue[numberOfTeams - x - 1]])

    out.insert(((i*(numberOfTeams//2) + 1)), [teamQueue[0] , numberOfTeams])
  
    teamQueue.append(teamQueue[0])
    teamQueue.popleft()


length = len(out)

out.append(['No team','No team'])    
out.append(['No team','No team'])

rounds = []

for i in range (0, length, 2):
    rounds.append((out[i][0], ",", out[i][1], "," ,out[i+1][0], ",", out[i+1][1]))
    print(out[i][0], ",", out[i][1], "," ,out[i+1][0], ",", out[i+1][1])

    if out[i][0] in [out[i-2][0],out[i-2][1],out[i-1][0],out[i-1][1]]:
        print("WARNING FOR TEAM: ", out[i][0])
        
    if out[i][1] in [out[i-2][0],out[i-2][1],out[i-1][0],out[i-1][1]]:
        print("WARNING FOR TEAM: ", out[i][1])
        
    if out[i+1][0] in [out[i-2][0],out[i-2][1],out[i-1][0],out[i-1][1]]:
        print("WARNING FOR TEAM: ", out[i+1][0])
        
    if out[i+1][1] in [out[i-2][0],out[i-2][1],out[i-1][0],out[i-1][1]]:
        print("WARNING FOR TEAM: ", out[i+1][1])

print(rounds)    
