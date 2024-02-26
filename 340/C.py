import math

n = int(input())
blackboard = []
blackboard.append(n)
cost = 0
# blackboard = sorted(blackboard)


while any(i >= 2 for i in blackboard):
    for i in range(len(blackboard)):
        if blackboard[i] >= 2:
            x = blackboard[i]
            cost += x
            del blackboard[i]
            blackboard.append(math.floor(x / 2))
            blackboard.append(math.ceil(x / 2))
            blackboard.sort()

print(cost)



# わからん。
# for i in range(1, len(blackboard)):
#     if blackbord[i] >= 2: