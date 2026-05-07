import tkinter as tk
from tkinter import messagebox

products = {
    "T-Shirt": 1500,
    "Jeans": 3000,
    "Jacket": 5000,
    "Shoes": 4000
}

cart = []

def add_to_cart():
    product = product_var.get()
    quantity = int(quantity_entry.get())
    price = products[product] * quantity
    cart.append((product, quantity, price))
    cart_list.insert(tk.END, f"{product} x{quantity} = Rs.{price}")

def checkout():
    total = sum(item[2] for item in cart)
    messagebox.showinfo("Checkout", f"Total Bill: Rs.{total}")

root = tk.Tk()
root.title("Clothing Brand POS System")
root.geometry("500x500")

tk.Label(root, text="Clothing POS System", font=("Arial", 18, "bold")).pack(pady=10)

product_var = tk.StringVar(value="T-Shirt")
tk.OptionMenu(root, product_var, *products.keys()).pack(pady=5)

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)
quantity_entry.insert(0, "1")

tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=10)

cart_list = tk.Listbox(root, width=40, height=10)
cart_list.pack(pady=10)

tk.Button(root, text="Checkout", command=checkout, bg="green", fg="white").pack(pady=20)

root.mainloop()
