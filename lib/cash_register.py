#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self._last_transaction_total = 0
    self._last_transaction_quantity = 0

  def add_item(self, title, price, quantity=1):
    amount = price * quantity
    self.total += amount
    for _ in range(quantity):
      self.items.append(title)
    self._last_transaction_total = amount
    self._last_transaction_quantity = quantity

  def apply_discount(self):
    if self.discount and self.discount > 0:
      self.total = self.total * (100 - self.discount) / 100
      # If total is a whole number, print without decimal
      if self.total.is_integer():
        print(f"After the discount, the total comes to ${int(self.total)}.")
      else:
        print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    # remove last transaction amount from total
    self.total -= self._last_transaction_total
    # remove the last transaction items from items list
    for _ in range(self._last_transaction_quantity):
      if self.items:
        self.items.pop()
    # reset last transaction
    self._last_transaction_total = 0
    self._last_transaction_quantity = 0
