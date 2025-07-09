#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prev_transactions = []       

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 <= value <= 100:
       self._discount = value
    else:
       raise ValueError("Not valid discount")    

  def add_item(self, item, price, quantity=1):  
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)    
    self.prev_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  def apply_discount(self):
    if not self.prev_transactions or not self.discount:
      print("There is no discount to apply.")
    else:
      discount_amount = (self.discount / 100) * self.total 
      self.total = round(self.total - discount_amount, 2)
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    
  def void_last_transaction(self):
    if not self.prev_transactions:
      print(f"There are no transactions to void")
    else:
      last_transaction = self.prev_transactions.pop()
      self.total -= last_transaction["price"] * last_transaction["quantity"]
    


