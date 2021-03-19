from random import randint

class game:
    first_in=enter_value=rand='' 
    def __init__(self):

        self.enter_value = int(input("Enter your random limit: "))
        self.rand = randint(1, self.enter_value)
        self.first_in = int(input(f"Enter a number from 1 - {self.enter_value} : "))
        self.func(self.calc, self.first_in)

    def func(self, func, val):
        while func(val) == True:
            i = input("Try again? (y/n) : ")
            if i in ['y', 'Y']:
                self.enter_value = int(input("Enter your random limit: "))
                self.rand = randint(1, self.enter_value)
                self.first_in = int(input(f"Enter a number from 1 - {self.enter_value} : "))
                self.calc(self.first_in)

            else:
                exit("Bye !!")

        else:
            print('Failed')

    def calc(self, number):
        return True if number == self.rand else False 

    def __str__(self):
        return self.rand

play = game()
print(play.__str__())
