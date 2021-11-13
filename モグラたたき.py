import time
import random

def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana= "."
        if i == r:
            ana= "o"
        m = m+"_"+ana+"_"
        n = n+"["+str(i)+"]"
    print(m)
    print(n)


print("=============　ゲームスタート　==============")
hit= 0
ts=time.time()
for i in range(10):
    r=random.randint(0,7)
    mogura(r)
    p = input("モグラはどこ")
    if p == str(r):
        print("Hit!!")
        hit = hit+1
else:
    print("MISS!!")
t=int(time.time()-ts)
bonus=0
if t<60:
    bonus=60-t

print("============== ゲームエンド ==============")
print("TIME",t,"sec")
print("HIT",hit,"×　Bonus",bonus)
print("SCORE",hit*bonus)
