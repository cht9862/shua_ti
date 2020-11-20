import model_1
import string
import random
from pprint import pprint
nm1 = model_1.eD()
nm2 = model_1.eE()
nm3 = model_1.eC()
def hello():

    liSt = []
    for i in range(1,11):
        str_i = str(i)
        liSt.append(str_i)
    nm_1 = []
    sm = 0
    while True:
        sm+=1
        if sm == 100:nm_1.clear()
        bad = []
        for i in range(10):
            print(nm_1)
            nm = random.choice(liSt)
            while True:
                if nm in nm_1:
                    nm = random.choice(liSt)
                else:
                    break
            nm_1.append(nm)
            nu = str(nm3[nm])
            print('='*60)
            print(nm1[nm],'\n')
            print(nm2[nm])
            a = str(input('输入选择的结果 ： '))
            if a == nu:
                print('回答正确，请开始下一题。\n')
                continue
            else:
                print(r'正确答案是: {}'.format(nm3[nm]))
                print('错题已记录，请继续下一题。 \n')
                test = str(r'标号：{}'.format(nm))
                bad.append(test)
                continue
            # input()
        print('\033[1;31m 以下是本次答题错误题目 ！！！!\n \033[0m')
        for j in bad:
            print(j, end='\t\t')
        print('')
        input('--&-- 任意按键继续答题. --&--')
hello()


