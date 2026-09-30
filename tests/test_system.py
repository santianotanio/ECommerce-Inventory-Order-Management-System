import sys
import tempfile
import unittest
from pathlib import Path

# Allow this test file to run both from the project root and directly:
#     python tests/test_system.py
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.models import Product
from app.storage import JSONStorage
from app.inventory import InventoryManager
from app.orders import OrderManager
from app.reports import ReportManager


class ECommerceTests(unittest.TestCase):
    def setUp(self):
        self.products = {
            "P1": Product("P1", "Test Mouse", "Electronics", 500, 10, 2),
            "P2": Product("P2", "Notebook", "Stationery", 100, 3, 3),
        }
        self.orders = {}
        self.inventory = InventoryManager(self.products)
        self.order_manager = OrderManager(self.products, self.orders)

    def test_add_product(self):
        self.inventory.add_product(Product("P3", "Pen", "Stationery", 20, 10))
        self.assertIn("P3", self.products)

    def test_duplicate_product_rejected(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product(Product("P1", "Another", "Other", 10, 1))

    def test_order_reduces_stock(self):
        order = self.order_manager.create_order("O1", "Alice", [("P1", 3)])
        self.assertEqual(order.total, 1500)
        self.assertEqual(self.products["P1"].stock, 7)

    def test_insufficient_stock_rejected(self):
        with self.assertRaises(ValueError):
            self.order_manager.create_order("O2", "Bob", [("P2", 5)])

    def test_cancel_restores_stock(self):
        self.order_manager.create_order("O3", "Cara", [("P1", 4)])
        self.order_manager.update_status("O3", "Cancelled")
        self.assertEqual(self.products["P1"].stock, 10)

    def test_low_stock(self):
        self.assertIn(self.products["P2"], self.inventory.low_stock())

    def test_json_persistence(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "store.json"
            storage = JSONStorage(str(path))
            storage.save(self.products, self.orders)
            loaded = storage.load_products()
            self.assertEqual(loaded["P1"].name, "Test Mouse")

    def test_reports(self):
        self.order_manager.create_order("O4", "Dev", [("P1", 2)])
        reports = ReportManager(self.products, self.orders)
        self.assertEqual(reports.sales_summary()["units_sold"], 2)
        self.assertEqual(reports.top_products()[0][0], "P1")


if __name__ == "__main__":
    unittest.main()
