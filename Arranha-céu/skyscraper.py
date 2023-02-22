N, Q = input().split()
N = int(N)
Q = int(Q)

floor = input().split()

output = "\n"

for i in range(0,Q):
    action = input().split()
    if(len(action) == 3):
        floor[(int(action[1])-1)] = int(action[2])
    elif(len(action) == 2):
        acum = 0
        for i in range(0, int(action[1])):
            acum += int(floor[i])
        output += str(acum)+"\n"
        
print(output)
        