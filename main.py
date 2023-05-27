import random

class EncapsulatedNumber:
    def __init__(self, value):
        self.value = value

    def perform_random_operation(self):
        self.value = random.randint(1, 100) * self.value

    def __str__(self):
        return str(self.value)


user_input = int(input("Введіть число: "))
number = EncapsulatedNumber(user_input)

number.perform_random_operation()
print(number)