# 인수로 전달한 정수를 반복해서 덧셈하는 프로입니다.
# 덧셈 결과 딱 100이 되었을 때는요.
# 'Just 100!'을 출력하세요.
# 100이 넘을 경우에는 그 시점에서 'Over!'입니다.
# 를 출력합니다
import sys

args = sys.argv
total = 0

while total < 100:
    value = int(args[1])
    total += value
if total == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")


# while total < 100:
#     value = int(input("値を入力してください: "))
#     total += value
#     print("現在の合計: ", total)
# if total == 100:
#     print("Just 100!")
# else:
#     print("Over!")