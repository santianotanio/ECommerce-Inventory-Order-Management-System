"""Reporting and lightweight analytics."""
from collections import Counter
from typing import Dict
from .models import Product, Order


class ReportManager:
    def __init__(self, products: Dict[str, Product], orders: Dict[str, Order]):
        self.products = products
        self.orders = orders

    def inventory_summary(self) -> dict:
        total_units = sum(p.stock for p in self.products.values())
        inventory_value = sum(p.stock * p.price for p in self.products.values())
        return {
            "products": len(self.products),
            "units": total_units,
            "inventory_value": round(inventory_value, 2),
            "low_stock": len([p for p in self.products.values() if p.stock <= p.reorder_level]),
        }

    def sales_summary(self) -> dict:
        active_orders = [o for o in self.orders.values() if o.status != "Cancelled"]
        revenue = sum(o.total for o in active_orders)
        units = sum(item.quantity for o in active_orders for item in o.items)
        status_counts = Counter(o.status for o in self.orders.values())
        return {
            "orders": len(active_orders),
            "revenue": round(revenue, 2),
            "units_sold": units,
            "status_counts": dict(status_counts),
        }

    def top_products(self) -> list:
        quantities = Counter()
        revenue = Counter()
        names = {}
        for order in self.orders.values():
            if order.status == "Cancelled":
                continue
            for item in order.items:
                quantities[item.product_id] += item.quantity
                revenue[item.product_id] += item.subtotal
                names[item.product_id] = item.product_name
        rows = []
        for pid, qty in quantities.items():
            rows.append((pid, names[pid], qty, round(revenue[pid], 2)))
        return sorted(rows, key=lambda x: (-x[2], -x[3], x[1].lower()))

    def customer_spending(self) -> list:
        spending = {}
        for order in self.orders.values():
            if order.status == "Cancelled":
                continue
            spending[order.customer_name] = spending.get(order.customer_name, 0) + order.total
        return sorted(
            [(name, round(total, 2)) for name, total in spending.items()],
            key=lambda x: (-x[1], x[0].lower()),
        )
