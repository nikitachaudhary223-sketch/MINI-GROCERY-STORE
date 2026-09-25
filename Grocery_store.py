products = {
    "Rice": 80,
    "Milk": 60,
    "Bread": 50,
    "Apple": 120,
    "Chocolate": 100
}

print("=" * 40)
print("        MINI GROCERY STORE")
print("=" * 40)

for item, price in products.items():
    print(item, "- Rs.", price)

cart = {}

# Shopping
while True:
    choice = input("\nEnter item (or 'done' to finish): ")

    if choice.lower() == "done":
        break

    if choice in products:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            cart[choice] = cart.get(choice, 0) + quantity
            print("Item added successfully!")
        else:
            print("Quantity must be greater than 0.")

    else:
        print("Item not available.")


# BILL
print("\n")
print("=" * 45)
print("               GROCERY BILL")
print("=" * 45)

subtotal = 0

for item, quantity in cart.items():
    price = products[item]
    total = price * quantity

    print(f"{item:<15} x {quantity:<3} = Rs. {total}")

    subtotal += total

# Discount
if subtotal >= 500:
    discount = subtotal * 0.10
else:
    discount = 0

amount_after_discount = subtotal - discount

# VAT
vat = amount_after_discount * 0.13

# Grand total
grand_total = amount_after_discount + vat

print("-" * 45)
print(f"{'Subtotal':<25} Rs. {subtotal:.2f}")
print(f"{'Discount':<25} Rs. {discount:.2f}")
print(f"{'Amount After Discount':<25} Rs. {amount_after_discount:.2f}")
print(f"{'VAT (13%)':<25} Rs. {vat:.2f}")
print("-" * 45)
print(f"{'GRAND TOTAL':<25} Rs. {grand_total:.2f}")
print("=" * 45)


# Payment
cash = float(input("Enter cash received: Rs. "))

if cash >= grand_total:
    change = cash - grand_total

    print(f"Cash Received: Rs. {cash:.2f}")
    print(f"Change: Rs. {change:.2f}")
    print("Payment successful!")
    print("Thank you for shopping!")

else:
    remaining = grand_total - cash

    print(f"Cash Received: Rs. {cash:.2f}")
    print(f"Insufficient cash.")
    print(f"Remaining amount: Rs. {remaining:.2f}")