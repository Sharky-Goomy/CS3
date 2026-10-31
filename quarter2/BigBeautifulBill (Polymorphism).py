class Bill:
    def __init__(self, amount):
        self.amount = amount
    def pay(self, payment):
        self.amount -= payment.amount
        print(f"Paying with {payment.mode}")
        print("Balance:", self.amount)

class Payment:
    amount = 0
    mode = "cash"
    def __init__(self, amount):
        self.amount = amount

class Ewallet(Payment):
    def __init__(self, name, amount):
        self.mode = name
        self.amount = amount

bigBeautifulBill = Bill(1000)
bayad = Payment(900)
bigBeautifulBill.pay(bayad)

gcash = Ewallet("GCash", 67)
bigBeautifulBill.pay(gcash)

PisayCash = Ewallet("PisayCash", 33)
bigBeautifulBill.pay(PisayCash)