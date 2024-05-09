arr = []
n = int(input())
m = int(input())

j = 1
end = -1

while True:
    arr.append(j)
    for i in range(1, m + 1):
        if i != m:
            if j < n:
                j = j + 1
            else:
                j = 1
        end = j
    if end == 1:
        break

print(*arr, sep='')
