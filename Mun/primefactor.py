import sys
n = int(sys.argv[1])

factors = []
# 2 で割り切れる部分をすべて取り出す
while n % 2 == 0:
    factors.append(2)
    n = n / 2
# 3以上の奇数で割り切れる部分を取り出す
for i in range(3,int(n**0.5)+1,2):
    while n % i == 0:
        factors.append(int(i))
        n = n / i
# 2と3以外の数で割り切れない場合、その数自体が素数である
if n > 2:
    factors.append(int(n))
    
print(factors,end="")

# print(prime_factorization(num))
# def prime_factorization(n):
#     factors = []
#     # 2 で割り切れる部分をすべて取り出す
#     while n % 2 == 0:
#         factors.append(2)
#         n = n / 2
#     # 3以上の奇数で割り切れる部分を取り出す
#     for i in range(3,int(n**0.5)+1,2):
#         while n % i == 0:
#             factors.append(int(i))
#             n = n / i
#     # 2と3以外の数で割り切れない場合、その数自体が素数である
#     if n > 2:
#         factors.append(int(n))
#     return factors

# # テスト
# num = int(input("素因数分解する数を入力してください: "))
# print(prime_factorization(num))
