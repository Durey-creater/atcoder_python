# URL:https://atcoder.jp/contests/abc338/tasks/abc338_b

from collections import Counter

s = input()

count = Counter(s)

# # 文字と出現回数を別々のリストに格納
text = list(count.keys())
frequencies = list(count.values())
print(text)