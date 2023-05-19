#!/usr/env python3

# 양자리가1마리,양자리가2마리,양자리가n마리로건넨정수의횟수만큼반복하는프로그램sheep.py 을개변한sheepfile.py 을만듭니다.
# 출력은 파일로 합니다.
# 출력할 파일의 파일명은 sheep.txt로 하는 것입니다.
# sheep.txt는 파일이 없으면 작성하고, 파일이 존재할 경우에는 실행 시마다 덮어쓰기 저장으로 합니다.

import sys

num = int(sys.argv[1])

# 引数回forを繰り返す
for i in range(num):
    # i + 1して出力する
    print(f"ひつじが{i+1}匹")
    
    
# def count_sheep(n):
#     with open('./files/sheep.txt', 'w') as f:
#         for i in range(1, n + 1):
#             f.write('ひつじが{}匹\n'.format(i))

# count_sheep(int(sys.argv[1]))

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print('使用方法: python sheepfile.py <整数>')
#     else:
#         count_sheep(int(sys.argv[1]))


