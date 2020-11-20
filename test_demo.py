import model_1
import string
import random
import os,sys

from pprint import pprint
nm1 = model_1.eD()
nm2 = model_1.eE()
nm3 = model_1.eC()
def hello():
    liSt = []
    numbers = 10
    for i in range(1,23):
        str_i = str(i)
        liSt.append(str_i)
    nm_1 = []
    sm = 0
    while True:
        if sm >= 1:nm_1.clear()
        sm += 1
        bad = []
        for i in range(22):
            os.system('cls')
            print('\n\n\n\n\n\n')
            print('')
            print('\033[1;31m #请将你的键盘调至为大写，本次答题将全部采用大写字母回答。\n \033[0m')
            nm = random.choice(liSt)
            while True:
                if nm in nm_1:
                    nm = random.choice(liSt)
                else:
                    break
            nm_1.append(nm)
            nu = str(nm3[nm])
            print('=='*50)
            print('\n',nm1[nm],'\n')
            print(nm2[nm],'\n\n')
            print('---' * 15)
            a = str(input('输入选择的结果 ： '))
            print('---' * 15)
            if a == nu:
                print('回答正确，请开始下一题。\n')
                input('--&-- 任意按键继续答题. --&--')
                continue
            else:
                print(r'正确答案是: {}'.format(nm3[nm]))
                print('错题已记录，请继续下一题。 \n')
                input('--&-- 任意按键继续答题. --&--')
                test = str(r'标号：{}'.format(nm))
                bad.append(test)
                continue
            # input()
        print('\033[1;31m 以下是本次答题错误题目 ！！！!\n \033[0m')
        for j in bad:
            print(j, end='   ')
            numbers += 1
            if numbers % 10 == 0: print('')
        print('\n')
        input('--&-- 任意按键继续答题. --&--')
hello()



