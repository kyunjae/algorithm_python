cash = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in changes:
    if cash == 0:
        break
    cnt += cash // i
    cash %= i

print(cnt)