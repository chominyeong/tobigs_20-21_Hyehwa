#11655
import sys
input = sys.stdin.readline

s = str(input())
answer = ''
for x in s:
  # 소문자
  if ('a'<=x) and (x<='z'):
    x = ord(x) + 13 #ord(): ASCII코드로 변환
    if x > 122:
      x -= 26
    answer += chr(x) #chr(): 정수로 변환

  # 대문자
  elif ('A'<=x) and (x<='Z'):
    x = ord(x) + 13
    if x > 90:
      x-=26
    answer += chr(x)

  # 숫자
  else: answer += x

print(answer)
