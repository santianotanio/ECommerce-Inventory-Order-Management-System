"""JSON-based persistence using only Python's standard library."""
import json
from pathlib import Path
from typing import Dict, List
from .models import Product, Order


class JSONStorage:
    """Stores products and orders in a single JSON file."""

    def __init__(self, file_path: str = "data/store.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def _empty_state(self) -> dict:
        return {"products": {}, "orders": {}}

    def load(self) -> dict:
        if not self.file_path.exists():
            return self._empty_state()
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, dict):
                return self._empty_state()
            data.setdefault("products", {})
            data.setdefault("orders", {})
            return data
        except (json.JSONDecodeError, OSError):
            return self._empty_state()

    def save(self, products: Dict[str, Product], orders: Dict[str, Order]) -> None:
        data = {
            "products": {pid: product.to_dict() for pid, product in products.items()},
            "orders": {oid: order.to_dict() for oid, order in orders.items()},
        }
        temporary = self.file_path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        temporary.replace(self.file_path)

    def load_products(self) -> Dict[str, Product]:
        data = self.load()
        return {pid: Product.from_dict(p) for pid, p in data["products"].items()}

    def load_orders(self) -> Dict[str, Order]:
        data = self.load()
        return {oid: Order.from_dict(o) for oid, o in data["orders"].items()}
