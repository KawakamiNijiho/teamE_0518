#!/bin/env python3

# 양자리가1마리,양자리가2마리,양자리가n마리로건넨정수의횟수만큼반복하는프로그램sheep.py 을개변한sheepfile.py 을만듭니다.
# 출력은 파일로 합니다.
# 출력할 파일의 파일명은 sheep.txt로 하는 것입니다.
# sheep.txt는 파일이 없으면 작성하고, 파일이 존재할 경우에는 실행 시마다 덮어쓰기 저장으로 합니다.

import sys

args = sys.argv 
count = int(args[1])

# 引数回forを繰り返す
for i in range(count):
    # i + 1して出力する
    sheep = i+1
    print("ひつじが",sheep,"匹")
    
    
def count_sheep(count):
    with open('./files/sheep.txt', 'w') as file:
        for i in range(1, count + 1):
            file.write('ひつじが{}匹\n'.format(i))
        file.close
        
count_sheep(int(args[1]))



