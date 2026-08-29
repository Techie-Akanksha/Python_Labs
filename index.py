#Invoice Generator

# Customer Name: John Doe
# Invoice Number: INV-1001
# products and services name
# Quantity
# price per item


Customer_Name = input("Enter Customer Name: ")
Invoice_Number = input("Enter Invoice Number: ")
Pro_Service_name = input("Enter Prodcts and Service Name: ")
Quantity = int(input("Enter Quantity: "))
Price =  int(input("Enter Price per Item: "))

Subtotal = Quantity * Price 
print("="*75)
print("                         INVOICE GENERATOR                         ")
print("="*75)
print()
print(f"Invoice Number: {Invoice_Number}")
print(f"Customer: {Customer_Name}")
print()


print(f"{'Item':<20}{'Qty':>5}{'Price':>10}{'Total':>10}") 
print("-" * 45) 
print(f"{Pro_Service_name:<20}{Quantity:>5}{Price:>10}{Subtotal:>10}") 
print() 
print("-" * 45) 
print(f"{'Subtotal:':>35} ₹{Subtotal}") 
print("=" * 45)