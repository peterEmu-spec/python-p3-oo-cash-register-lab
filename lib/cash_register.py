#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        # Store last transaction as a dictionary
        self.last_transaction = {"title": title, "price": price, "quantity": quantity}
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            self.total -= (self.discount / 100) * self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
            for _ in range(self.last_transaction["quantity"]):
                if self.items:
                    self.items.pop()
            self.last_transaction = None

        if not self.items:
            self.total = 0.0
