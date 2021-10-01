if __name__ == '__main__':
    a = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        a += (name,score)
k=100.00
for i in range(1,(n*2),2):
    if a[i] < k:
        k = a[i]
for i in range(1,(n*2),2):
    if a[i] == k:
        a[i] = 100
k=100
for i in range(1,(n*2),2):
    if a[i] < k:
        k = a[i]
j = []
for i in range(1,(n*2),2):
    if a[i] == k:
        j.append(a[i-1])
j.sort()
for i in j:
    print(i)
