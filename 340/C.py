import math

n = int(input())
blackboard = []
blackboard.append(n)
cost = 0
# blackboard = sorted(blackboard)


while blackboard:
    max_blackboard = max(blackboard)
    if max_blackboard >= 2:
        x = max_blackboard
        cost += x
        blackboard.append(math.floor(x / 2))
        blackboard.append(math.ceil(x / 2))
        blackboard.remove(x)
    if max_blackboard < 2:
        break

print(cost)

#    for i in range(len(blackboard)):
#         if blackboard[i] >= 2:
#             x = blackboard[i]
#             cost += x
#             del blackboard[i]
#             blackboard.append(math.floor(x / 2))
#             blackboard.append(math.ceil(x / 2))
#             # blackboard.sort()

# print(cost)


