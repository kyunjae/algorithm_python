from sys import stdin

T = int(input())

for i in range(T):
    N = int(stdin.readline())
    rank = [list(map(int, stdin.readline().split())) for _ in range(N)]
    people = sorted(rank)
    top = 0
    cnt = 1

    for i in range(1, len(people)):
        if people[i][1] < people[top][1]:
            top = i
            cnt += 1

    print(cnt)