a1 = int(input())
a2 = int(input())
a3 = int(input())
andar1 = a1*0 + a2*2 + a3*4
andar2 = a2*0 + a1*2 + a3*2
andar3 = a3*0 + a1*4 + a2*2
if (andar1 <= andar2 and andar1 <= andar3):
    print(andar1)
elif (andar2 <= andar1 and andar2 <= andar3):
    print(andar2)
elif (andar3 <= andar2 and andar3 <= andar1):
    print(andar3)