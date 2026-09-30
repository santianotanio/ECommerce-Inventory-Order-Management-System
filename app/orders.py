"""Order processing service."""
from typing import Dict, List
from .models import Order, OrderItem, Product
from .validators import required_text


VALID_STATUSES = ("Pending", "Processing", "Shipped", "Delivered", "Cancelled")


class OrderManager:
    def __init__(self, products: Dict[str, Product], orders: Dict[str, Order]):
        self.products = products
        self.orders = orders

    def create_order(self, order_id: str, customer_name: str, cart: List[tuple]) -> Order:
        order_id = required_text(order_id, "Order ID").upper()
        customer_name = required_text(customer_name, "Customer name")

        if order_id in self.orders:
            raise ValueError("An order with this ID already exists.")
        if not cart:
            raise ValueError("An order must contain at least one product.")

        items = []
        requested = {}
        for product_id, quantity in cart:
            product_id = product_id.strip().upper()
            if product_id not in self.products:
                raise KeyError(f"Product '{product_id}' was not found.")
            if quantity <= 0:
                raise ValueError("Order quantity must be greater than zero.")
            requested[product_id] = requested.get(product_id, 0) + quantity

        for product_id, quantity in requested.items():
            product = self.products[product_id]
            if product.stock < quantity:
                raise ValueError(
                    f"Insufficient stock for {product.name}. Available: {product.stock}."
                )

        for product_id, quantity in requested.items():
            product = self.products[product_id]
            product.stock -= quantity
            items.append(OrderItem(product_id, product.name, quantity, product.price))

        order = Order(order_id, customer_name, items)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: str) -> Order:
        order_id = required_text(order_id, "Order ID").upper()
        if order_id not in self.orders:
            raise KeyError(f"Order '{order_id}' was not found.")
        return self.orders[order_id]

    def update_status(self, order_id: str, status: str) -> Order:
        order = self.get_order(order_id)
        status = status.strip().title()
        if status not in VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(VALID_STATUSES)}.")
        if order.status == "Cancelled":
            raise ValueError("A cancelled order cannot be changed.")
        if status == "Cancelled":
            for item in order.items:
                self.products[item.product_id].stock += item.quantity
        order.status = status
        return order

    def list_orders(self) -> List[Order]:
        return sorted(self.orders.values(), key=lambda x: x.order_id)
