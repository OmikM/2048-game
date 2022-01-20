import random
plansza = [0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0]
def display2048():
  for i in range(4):
    print(plansza[i*4+0]," ",plansza[i*4+1]," ",plansza[i*4+2]," ",plansza[i*4+3]," ")
def SpawnNew():
  posPlace = []
  for i in range(16):
    if plansza[i]==0:
      posPlace.append(i)
  print(posPlace)
  plansza[random.choice(posPlace)]=(int(random.choice("248")))
def moveUp():
  for x in range(4):
    for i in range(3):
      if plansza[8-i*4+x]==0:
        plansza[8-i*4+x]=plansza[12-i*4+x]
        plansza[12-i*4+x] = 0
      elif plansza[8-i*4+x]==plansza[12-i*4+x]:
        plansza[8-i*4+x]=plansza[12-i*4+x]*2
        plansza[12-i*4+x] = 0
while True:
 # print("______________")
 # display2048()
 # print("______________")
  SpawnNew()
  display2048()
  odp = input()
  if odp=='w':
    SpawnNew()