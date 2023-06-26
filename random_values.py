import random
# members=["Amal","Maya","Jumana","Elias"]
# leader=random.choice(members)
# print(leader)

# numbers=[1,2,3,4,5,6]
# ch=random.choice(numbers)
# ch2=random.choice(numbers)
#
# print(f"({ch},{ch2})")

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dice = Dice()
print(dice.roll())