# URL:https://atcoder.jp/contests/abc339/tasks/abc339_b

# h, w, nをinputで受け取る。splitで空白ごとに分割、
h, w, n = map(int, input().split())

# 右、左、上、下へ移動するためのリストを生成
vector =[(0,1),(1,0),(0,-1),(-1,0)]

# 初期状態のgridを生成
# ”.”をw個for文でリストに追加し、そのリストをh個for文でリストに追加
grid = [['.' for _ in range(w)] for _ in range(h)]
# grid = []
# for _ in range(h):
#     row = []
#     grid.append(row)
#     for _ in range(w):
#         row.append('.')

# 初期座標をx, にそれぞれ格納
x, y, v = 0, 0, 0
for i in range(n):
    if grid[x][y] == '.':
        grid[x][y] = '#'
        v = (v + 1) % 4
        x += vector[v][0]
        y += vector[v][1]
    else:
        grid[x][y] = '.'
        v = (v - 1) % 4
        x += vector[v][0]
        y += vector[v][1]
    x = (x + vector[v][0]) % h
    y = (y + vector[v][1]) % w
    
print(grid)

