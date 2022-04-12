from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="052"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc067_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''1
'''
y = '''
'''
additional_case = [x]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import defaultdict
  import math
  def Eratosthenes(n):
    prime=[]
    furui=list(range(2,n+1))
    while furui[0]<math.sqrt(n):
      prime.append(furui[0])
      furui=[i for i in furui if i%furui[0]!=0]
    return prime+furui
  mod=10**9+7
  N=int(input())
  if N==1: print(1)
  else: 
    E=Eratosthenes(N)
    d=defaultdict(int)
    ans=1
    for n in range(N):
      tmp=n+1
      for i in range(len(E)):
        while tmp%E[i]==0: tmp//=E[i]; d[E[i]]+=1
    for k in d:
      ans=(ans*(d[k]+1))%mod
    print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])