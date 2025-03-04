n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = list()

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)