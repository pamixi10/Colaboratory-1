import random
r=random.random()
print(r)
r=random.randint(1,6)
print(r)
jan=random.choice(["グー","チョキ","パー"])
print(jan)
count=0
while True:
     r=random.randint(1,100)
     print(r)
     count=count+1
     if r==77:
          break
print(f"{count}回目でレアキャラをゲット")
