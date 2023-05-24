import sys

class IntroFam:
    def __init__(self, name, age, pet_name):
        self.name = name
        self.age = age
        self.pet_name = pet_name

    def introduce(self):
        return f"私の名前は{self.name}です。年齢は{self.age}歳です。家族の一員に愛猫の{self.pet_name}がいます。"

# コマンドライン引数から名前、年齢、飼い猫の名前を取得
name = sys.argv[1]
age = sys.argv[2]
pet_name = sys.argv[3]

# IntroFam クラスのインスタンスを生成
person = IntroFam(name, age, pet_name)

# 自己紹介文の出力
print(person.introduce())