# URL:https://atcoder.jp/contests/abc338/tasks/abc338_a

# 文字列を受け取る
s = input()
result = "No"
 
# 1文字目が小文字 
if s[0].islower():
    result = "No"
# 1文字目が大文字
else:
    # 文字列の長さが1文字
    if len(s) == 1:
        result = "Yes"
    # 文字列の長さが2文字以上
    else:
        for i in range (1, len(s)):
            # 2文字目移行に小文字が含まれるかどうか
            if s[i].islower():
                result = "Yes"
            else:
                result = "No"
                break
print(result)