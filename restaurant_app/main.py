import tkinter as tk
from tkinter import messagebox, ttk

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Menu")

        # Labels and Inputs
        tk.Label(root, text="Pizza Quantity").grid(row=0, column=0, padx=10, pady=5)
        self.pizza_qty = tk.Entry(root)
        self.pizza_qty.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Pizza Size").grid(row=1, column=0, padx=10, pady=5)
        self.pizza_size = ttk.Combobox(root, values=["Small", "Medium", "Large"])
        self.pizza_size.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Burger Quantity").grid(row=2, column=0, padx=10, pady=5)
        self.burger_qty = tk.Entry(root)
        self.burger_qty.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Burger Size").grid(row=3, column=0, padx=10, pady=5)
        self.burger_size = ttk.Combobox(root, values=["Classic", "Big"])
        self.burger_size.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Soft Drink Quantity").grid(row=4, column=0, padx=10, pady=5)
        self.soft_drink_qty = tk.Entry(root)
        self.soft_drink_qty.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Order Type").grid(row=5, column=0, padx=10, pady=5)
        self.order_type = tk.StringVar()
        tk.Radiobutton(root, text="Takeaway", variable=self.order_type, value="Takeaway").grid(row=5, column=1, padx=10, pady=5)
        tk.Radiobutton(root, text="Dine In", variable=self.order_type, value="Dine In").grid(row=5, column=2, padx=10, pady=5)

        self.extra_cheese = tk.BooleanVar()
        tk.Checkbutton(root, text="Extra Cheese", variable=self.extra_cheese).grid(row=6, column=0, padx=10, pady=5)

        self.extra_ketchup = tk.BooleanVar()
        tk.Checkbutton(root, text="Extra Ketchup", variable=self.extra_ketchup).grid(row=6, column=1, padx=10, pady=5)

        tk.Button(root, text="Order Summary", command=self.show_summary).grid(row=7, column=0, columnspan=2, padx=10, pady=20)

    def show_summary(self):
        pizza_qty = int(self.pizza_qty.get())
        pizza_size = self.pizza_size.get()
        burger_qty = int(self.burger_qty.get())
        burger_size = self.burger_size.get()
        soft_drink_qty = int(self.soft_drink_qty.get())
        order_type = self.order_type.get()
        extra_cheese = self.extra_cheese.get()
        extra_ketchup = self.extra_ketchup.get()

        summary = f"Order Summary:\nPizza: {pizza_qty} {pizza_size}\nBurger: {burger_qty} {burger_size}\nSoft Drinks: {soft_drink_qty}\nOrder Type: {order_type}\n"
        if extra_cheese:
            summary += "Extra Cheese\n"
        if extra_ketchup:
            summary += "Extra Ketchup\n"

        total_price = (pizza_qty * {"Small": 5, "Medium": 7, "Large": 10}[pizza_size] +
                       burger_qty * {"Classic": 5, "Big": 7}[burger_size] +
                       soft_drink_qty * 2 +
                       extra_cheese * 1 +
                       extra_ketchup * 1)

        summary += f"Total Price: ${total_price}"
        messagebox.showinfo("Order Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
