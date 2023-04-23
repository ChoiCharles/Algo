import sys
input = sys.stdin.readline

def preorder(idx):
    if lst[idx] == 0:
        return
    print(lst[idx], end='')
    preorder(idx*2)
    preorder(idx*2+1)

def inorder(idx):
    if lst[idx] == 0:
        return
    inorder(idx*2)
    print(lst[idx], end='')
    inorder(idx*2+1)

def postorder(idx):
    if lst[idx] == 0:
        return
    postorder(idx*2)
    postorder(idx*2+1)
    print(lst[idx], end='')

n = int(input())
lst = [0] * 1000
lst[1] = 'A'
for i in range(n):
    a, b, c = input().split()
    idx = lst.index(a)
    if b != '.':
        lst[idx*2] = b
    if c != '.':
        lst[idx*2+1] = c
preorder(1)
print()
inorder(1)
print()
postorder(1)