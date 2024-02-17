# URL:https://atcoder.jp/contests/abc340/tasks/abc340_b

A = []

for i in range(int(input())):
    query, x = map(int, input().split())
    if query == 1:
        A.append(x)
    elif query == 2:
        print(A[-x])