# Getter and setter method
class BankAcc:
    def __init__(self):
        self.__balance =  400  #  --- to make private use -->__balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > 0 :
            self.__balance = amount

b = BankAcc()
print(b.get_balance())
b.set_balance(100)
print(b.get_balance())
# directly accessing private variable ---> name mangaling
print(b._BankAcc__balance)