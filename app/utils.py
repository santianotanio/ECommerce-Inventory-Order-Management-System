"""Console presentation helpers."""
from datetime import datetime


def money(value: float) -> str:
    return f"₹{value:,.2f}"


def line(char="─", width=78) -> str:
    return char * width


def title(text: str) -> None:
    print("\n" + line("═"))
    print(f"  {text}")
    print(line("═"))


def pause() -> None:
    input("\nPress Enter to continue...")


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_products(products) -> None:
    if not products:
        print("No products found.")
        return
    print(f"{'ID':<10}{'Product':<25}{'Category':<18}{'Price':>12}{'Stock':>8}")
    print(line())
    for p in products:
        print(f"{p.product_id:<10}{p.name[:24]:<25}{p.category[:17]:<18}"
              f"{money(p.price):>12}{p.stock:>8}")


def print_orders(orders) -> None:
    if not orders:
        print("No orders found.")
        return
    for order in orders:
        print(f"\n{order.order_id} | {order.customer_name} | {order.status} | {money(order.total)}")
        for item in order.items:
            print(f"   - {item.product_name} × {item.quantity} = {money(item.subtotal)}")
