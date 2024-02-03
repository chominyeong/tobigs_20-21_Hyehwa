#1436
import sys
input = sys.stdin.readline
x = int(input())
dp = [0]*(x+1)

for i in range(2, x+1):
  #⑴ 1을 빼는 연산
  dp[i] = dp[i-1] + 1
  #⑵ 2로 나누어 떨어지는지 확인
  if i%2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1)
    ##1을 뺐었을 때 연산 횟수와 2로 나눴을 연산 횟수 중 최소를 채택
  #⑶ 3으로 나누어 떨어지는지 확인
  if i%3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)

print(dp[x])