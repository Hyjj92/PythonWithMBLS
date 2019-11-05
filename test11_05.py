import os
import time
import random


def horseRace():
    # 利用字符串切片操作实现跑马灯效果
    string = '寒蝉凄切，对长亭晚，骤雨初歇，*******'
    i = 1
    while i < 50:
        os.system("cls")
        # huozhe  os.system("clear")
        print(string)
        string = string[1:]+ string[0]
        time.sleep(0.2)
        i = i + 1
    os.system('clear')

def identifying_code():
    # 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
    # 假设验证码长度为4(定义为 long_code )
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_char = len(chars) - 1
    long_code = 4
    code = ''
    for _ in range(long_code):
        index = random.randint(0,num_char)
        code = code + chars[index]
    print('验证码是',code )



def main():    
    horseRace()
    identifying_code()


if __name__ == '__main__':
    main()