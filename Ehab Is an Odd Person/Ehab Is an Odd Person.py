n = int(input())
a = list(map(int, input().split()))
first = 0
second = 0


for i in range(n):
    if a[i] % 2 == 1:
        first = 1
    else:
        second = 1

    if second and first:
        a.sort()

for i in range(n):
    print(a[i], end=" ")
print()


