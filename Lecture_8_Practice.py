# 1) create student class that takes name & marks of 3 subjects as arguments in constructor.
#    Then create a method to print the average.

class Student:
    def __init__(self, name, marks):     # assume marks here is a list
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is: ", sum/3)

s1 = Student("Abhishek", [98, 96, 93])
s1.get_avg()          # hi Abhishek your avg score is:  95.66666666666667

# For changing the name in the attribute

s1.name = "Adil"
s1.get_avg()          # hi Adil your avg score is:  95.66666666666667

# 2) Create Account class with 2 attributes - balance and account no.
#    Create method for debit, credit and printing the balance

class Account:
    # class with 2 attributes - balance and account no.
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total balance = ", self.get_balance())     # internal method ko hi call kr liya 
    
    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credited")
        print("total balance = ", self.get_balance())

    # printing balance method
    def get_balance(self):
        return self.balance

# object for the class
acc1 = Account(10000, 12345)     # acc1 means account 1
print(acc1.balance)
print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)
acc1.debit(4000)

'''OUTPUT
10000
12345
Rs.  1000 was debited
total balance =  9000
Rs.  500 was credited
total balance =  9500
Rs.  4000 was credited
total balance =  13500
Rs.  4000 was debited
total balance =  9500
'''
