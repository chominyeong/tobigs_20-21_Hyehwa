#1934
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result = A*B #최소공배수가 될 수 있는 값 중 최대

    while B>0:
        A,B = B, A%B

    print(result//A)
