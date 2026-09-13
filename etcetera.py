#TODO:
#set - unordered, mutable, non-hashable, non-indexable, NO DUPLICATES

# students = [{"name": "harry", "house": "gryfindor"}, {"name": "hermoine", "house": "slytherin"}]

# # houses = []

# # for student in students:
# #     if student["house"] not in houses:
# #         houses.append(student["house"])

# # for house in houses:
# #     print(house)

# houses = set()                 #set uses add instead of append like list

# for student in students:
#     if student["house"] not in houses:
#         houses.add(student["house"])

# for house in sorted(houses):
#     print(house)

#TODO:

#gobal variables

# balance = 0 

# def main():
#     print("balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("balance:", balance)

# def deposit(amount):
#     global balance      # if a variable is defined inside main function or any function that has been then its fine, TODO: BUT!
#     balance += amount

# def withdraw(amount):   # BUT! if a variable is defined outside of functions i.e, global. to call it in function use TODO: global variable
#     global balance
#     balance -= amount

# if __name__ == "__main__":
#     main()

#TODO: best option is to write inside a class for these kind of functions. As they are related

class Bank:
    def __init__(self):
        amount = int(input("Enter a value: "))
        self.balance = amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("not allowed")
        self._balance = amount

    def withdraw(self, amount):
        if amount < self._balance:
            self.balance -= amount

    def __str__(self):
        return f"{self.balance} is your balance"

def main():
    account = Bank()
    print(account.balance)
    # account.deposit(100)
    account.withdraw(50)
    print(account.balance)

if __name__ == "__main__":
    main()

