# 水仙花数
for num in range(100,1000):
    low = num % 10
    mid = (num // 10)%10
    hig = num // 100
    if num == low**3+mid**3+hig**3:
        print(num)

# 正整数反转
num = int(input ('num =') )
reversal_num = 0
while num >0:
    reversal_num = reversal_num *10 + num %10
    num = num // 10
print(reversal_num)

'''百鸡百钱问题
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
'''
sum = 100
money = 100
for jiwong in range(0,20):
    for muji in range (0,34):
        xiaoji = sum - jiwong -muji
        if money == jiwong *5 + muji *3 + xiaoji/3:
            print("jiwong = ",jiwong,"muji = ",muji ,"xiaoji = ",xiaoji)

'''CRAPS
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
'''
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
        else:
            print("下注金额大于你的资产")
            continue
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')