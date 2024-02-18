# URL:https://atcoder.jp/contests/abc339/tasks/abc339_b

# h, w, nをinputで受け取る。splitで空白ごとに分割、
h, w, n = map(int, input().split())

# 上、右、下、左へ移動するためのリストを生成
vector =[(0,-1),(1,0),(0,1),(-1,0)]

# 初期状態のgridを生成
# ”.”をw個for文でリストに追加し、そのリストをh個for文でリストに追加
grid = [['.' for _ in range(w)] for _ in range(h)]
# grid = []
# for _ in range(h):
#     row = []
#     grid.append(row)
#     for _ in range(w):
#         row.append('.')

# 初期座標をx, yに、向いている方向(vector)の初期情報をvに代入
x, y, v = 0, 0, 0
for i in range(n):
    # 座標のが”.”の場合
    if grid[y][x] == '.':
        # ”#”に変更
        grid[y][x] = '#'
        # 向いている方向を変更
        v = (v + 1) % 4
    else: 
        grid[y][x] = '.'
        v = (v - 1) % 4
    
    #vx, vyに座標の移動量を代入
    vx, vy = vector[v]
    # 移動量を足して、h, wで割った余りを代入(トーラス状にするため)
    x = (x + vx) % w
    y = (y + vy) % h

# gridリストの各行をfor文で出力
# *で要素を展開して、sepで空白なしで出力する。
for j in grid:
    print(*j, sep='')

