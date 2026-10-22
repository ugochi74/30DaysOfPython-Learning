user_name = "codo"
def calculate_total_price(item_price, tax_rate):
      return item_price + (item_price * tax_rate)

price = 200.00
tax = 0.05
final_price = calculate_total_price(price, tax)
print(f"Hello {user_name}, your total price is: ₦{final_price}")