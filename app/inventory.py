"""Inventory management service."""
from typing import Dict, List
from .models import Product
from .validators import required_text


class InventoryManager:
    def __init__(self, products: Dict[str, Product]):
        self.products = products

    def add_product(self, product: Product) -> None:
        if product.product_id in self.products:
            raise ValueError("A product with this ID already exists.")
        if product.stock < 0:
            raise ValueError("Stock cannot be negative.")
        if product.price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.products[product.product_id] = product

    def get_product(self, product_id: str) -> Product:
        product_id = required_text(product_id, "Product ID").upper()
        if product_id not in self.products:
            raise KeyError(f"Product '{product_id}' was not found.")
        return self.products[product_id]

    def update_product(self, product_id: str, **changes) -> Product:
        product = self.get_product(product_id)
        for key, value in changes.items():
            if value is not None and hasattr(product, key):
                setattr(product, key, value)
        if product.price <= 0 or product.stock < 0 or product.reorder_level < 0:
            raise ValueError("Price/stock/reorder level values are invalid.")
        return product

    def delete_product(self, product_id: str) -> None:
        product = self.get_product(product_id)
        del self.products[product.product_id]

    def search(self, keyword: str = "") -> List[Product]:
        keyword = keyword.strip().lower()
        return [
            p for p in self.products.values()
            if keyword in p.name.lower()
            or keyword in p.category.lower()
            or keyword in p.product_id.lower()
        ]

    def low_stock(self) -> List[Product]:
        return sorted(
            [p for p in self.products.values() if p.stock <= p.reorder_level],
            key=lambda p: (p.stock, p.name.lower()),
        )

    def restock(self, product_id: str, quantity: int) -> Product:
        product = self.get_product(product_id)
        if quantity <= 0:
            raise ValueError("Restock quantity must be greater than zero.")
        product.stock += quantity
        return product
