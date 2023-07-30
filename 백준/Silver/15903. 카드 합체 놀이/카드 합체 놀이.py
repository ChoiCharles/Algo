from queue import PriorityQueue

q = PriorityQueue()
n, m = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    q.put(i)
for i in range(m):
    a = q.get()
    b = q.get()
    c = a + b
    q.put(c)
    q.put(c)
ans = 0
for i in range(n):
    ans += q.get()
print(ans)