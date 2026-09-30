"""Interactive command-line application."""
from .models import Product
from .storage import JSONStorage
from .inventory import InventoryManager
from .orders import OrderManager
from .reports import ReportManager
from .orders import VALID_STATUSES
from .validators import (
    required_text, positive_int, non_negative_int, positive_float
)
from .utils import title, pause, money, print_products, print_orders


class ECommerceSystem:
    def __init__(self):
        self.storage = JSONStorage()
        self.products = self.storage.load_products()
        self.orders = self.storage.load_orders()
        self.inventory = InventoryManager(self.products)
        self.order_manager = OrderManager(self.products, self.orders)
        self.reports = ReportManager(self.products, self.orders)

    def save(self):
        self.storage.save(self.products, self.orders)

    def seed_if_empty(self):
        if self.products:
            return
        samples = [
            Product("P1001", "Wireless Mouse", "Electronics", 699, 25, 5),
            Product("P1002", "Mechanical Keyboard", "Electronics", 2499, 12, 4),
            Product("P1003", "USB-C Cable", "Accessories", 399, 40, 10),
            Product("P1004", "Laptop Stand", "Accessories", 1299, 8, 3),
            Product("P1005", "Notebook", "Stationery", 149, 30, 8),
        ]
        for product in samples:
            self.inventory.add_product(product)
        self.save()

    def add_product(self):
        title("Add Product")
        try:
            pid = required_text(input("Product ID: "), "Product ID").upper()
            name = required_text(input("Product name: "), "Product name")
            category = required_text(input("Category: "), "Category")
            price = positive_float(input("Price (₹): "), "Price")
            stock = non_negative_int(input("Opening stock: "), "Opening stock")
            reorder = non_negative_int(input("Reorder level: "), "Reorder level")
            self.inventory.add_product(Product(pid, name, category, price, stock, reorder))
            self.save()
            print("✓ Product added successfully.")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def view_inventory(self):
        title("Inventory")
        print_products(self.inventory.search())
        pause()

    def search_products(self):
        title("Search Products")
        keyword = input("Search by ID, name or category: ")
        print_products(self.inventory.search(keyword))
        pause()

    def update_product(self):
        title("Update Product")
        try:
            pid = input("Product ID: ").strip().upper()
            product = self.inventory.get_product(pid)
            print(f"Current: {product.name} | {money(product.price)} | Stock {product.stock}")
            name = input("New name (Enter to keep): ").strip()
            price_text = input("New price (Enter to keep): ").strip()
            stock_text = input("New stock (Enter to keep): ").strip()
            reorder_text = input("New reorder level (Enter to keep): ").strip()
            changes = {}
            if name:
                changes["name"] = name
            if price_text:
                changes["price"] = positive_float(price_text, "Price")
            if stock_text:
                changes["stock"] = non_negative_int(stock_text, "Stock")
            if reorder_text:
                changes["reorder_level"] = non_negative_int(reorder_text, "Reorder level")
            self.inventory.update_product(pid, **changes)
            self.save()
            print("✓ Product updated.")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def delete_product(self):
        title("Delete Product")
        try:
            pid = input("Product ID: ").strip().upper()
            product = self.inventory.get_product(pid)
            if any(item.product_id == pid for order in self.orders.values() for item in order.items):
                print("✗ This product appears in order history and cannot be deleted.")
            elif input(f"Delete '{product.name}'? (yes/no): ").strip().lower() == "yes":
                self.inventory.delete_product(pid)
                self.save()
                print("✓ Product deleted.")
            else:
                print("Deletion cancelled.")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def restock(self):
        title("Restock Product")
        try:
            pid = input("Product ID: ").strip().upper()
            quantity = positive_int(input("Quantity to add: "), "Quantity")
            product = self.inventory.restock(pid, quantity)
            self.save()
            print(f"✓ {product.name} now has {product.stock} units.")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def low_stock_report(self):
        title("Low Stock Alert")
        products = self.inventory.low_stock()
        if not products:
            print("✓ All products are above their reorder levels.")
        else:
            print_products(products)
        pause()

    def create_order(self):
        title("Create Order")
        try:
            oid = input("Order ID: ")
            customer = input("Customer name: ")
            cart = []
            print("Enter items. Leave Product ID empty when finished.")
            while True:
                pid = input("Product ID: ").strip()
                if not pid:
                    break
                qty = positive_int(input("Quantity: "), "Quantity")
                cart.append((pid, qty))
            order = self.order_manager.create_order(oid, customer, cart)
            self.save()
            print(f"\n✓ Order {order.order_id} created.")
            print(f"Customer: {order.customer_name}")
            print(f"Total: {money(order.total)}")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def view_orders(self):
        title("Order History")
        print_orders(self.order_manager.list_orders())
        pause()

    def update_order_status(self):
        title("Update Order Status")
        try:
            oid = input("Order ID: ")
            print("Allowed:", ", ".join(VALID_STATUSES))
            status = input("New status: ")
            order = self.order_manager.update_status(oid, status)
            self.save()
            print(f"✓ {order.order_id} is now {order.status}.")
        except (ValueError, KeyError) as exc:
            print(f"✗ {exc}")
        pause()

    def dashboard(self):
        title("Business Dashboard")
        inventory = self.reports.inventory_summary()
        sales = self.reports.sales_summary()
        print(f"Products in catalogue : {inventory['products']}")
        print(f"Units currently held  : {inventory['units']}")
        print(f"Inventory value       : {money(inventory['inventory_value'])}")
        print(f"Low-stock products    : {inventory['low_stock']}")
        print(f"\nActive orders         : {sales['orders']}")
        print(f"Units sold            : {sales['units_sold']}")
        print(f"Recorded revenue      : {money(sales['revenue'])}")
        print(f"Order statuses        : {sales['status_counts']}")
        pause()

    def top_products(self):
        title("Top-Selling Products")
        rows = self.reports.top_products()
        if not rows:
            print("No sales recorded yet.")
        else:
            print(f"{'ID':<10}{'Product':<28}{'Units':>8}{'Revenue':>15}")
            print("-" * 61)
            for pid, name, units, revenue in rows:
                print(f"{pid:<10}{name[:27]:<28}{units:>8}{money(revenue):>15}")
        pause()

    def run(self):
        self.seed_if_empty()
        while True:
            title("E-Commerce Inventory & Order Management System")
            print("1. View Inventory")
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Search Products")
            print("6. Restock Product")
            print("7. Low Stock Alerts")
            print("8. Create Order")
            print("9. View Orders")
            print("10. Update Order Status")
            print("11. Business Dashboard")
            print("12. Top-Selling Products")
            print("0. Exit")
            choice = input("\nChoose an option: ").strip()

            actions = {
                "1": self.view_inventory,
                "2": self.add_product,
                "3": self.update_product,
                "4": self.delete_product,
                "5": self.search_products,
                "6": self.restock,
                "7": self.low_stock_report,
                "8": self.create_order,
                "9": self.view_orders,
                "10": self.update_order_status,
                "11": self.dashboard,
                "12": self.top_products,
            }
            if choice == "0":
                self.save()
                print("\nThank you for using the system.")
                break
            action = actions.get(choice)
            if action:
                action()
            else:
                print("✗ Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    ECommerceSystem().run()
