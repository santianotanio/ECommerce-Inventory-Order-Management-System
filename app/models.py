"""Domain models for the inventory and order management system."""
from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class Product:
    product_id: str
    name: str
    category: str
    price: float
    stock: int
    reorder_level: int = 5

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(
            product_id=str(data["product_id"]),
            name=str(data["name"]),
            category=str(data["category"]),
            price=float(data["price"]),
            stock=int(data["stock"]),
            reorder_level=int(data.get("reorder_level", 5)),
        )


@dataclass
class OrderItem:
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_price, 2)

    def to_dict(self) -> dict:
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "OrderItem":
        return cls(
            product_id=str(data["product_id"]),
            product_name=str(data["product_name"]),
            quantity=int(data["quantity"]),
            unit_price=float(data["unit_price"]),
        )


@dataclass
class Order:
    order_id: str
    customer_name: str
    items: List[OrderItem]
    status: str = "Pending"

    @property
    def total(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": [item.to_dict() for item in self.items],
            "status": self.status,
            "total": self.total,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Order":
        return cls(
            order_id=str(data["order_id"]),
            customer_name=str(data["customer_name"]),
            items=[OrderItem.from_dict(x) for x in data.get("items", [])],
            status=str(data.get("status", "Pending")),
        )
