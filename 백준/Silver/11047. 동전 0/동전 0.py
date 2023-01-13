n, k = map(int, input().split())
coin_list = []

for i in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.reverse()
cnt = 0

for coin in coin_list:
    cnt = cnt + k // coin
    k = k % coin

print(cnt)