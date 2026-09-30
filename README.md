# 🛒 E-Commerce Inventory & Order Management System

> A modular, menu-driven e-commerce back-office application built entirely with Python's standard library.

---

## 📌 Project Overview

The **E-Commerce Inventory & Order Management System** is a Python-based application designed to help a small online business manage its products, inventory, customer orders, order statuses, and basic business reports from one centralized system.

In a typical small e-commerce operation, inventory and orders may be tracked manually using spreadsheets, notes, or separate records. This can lead to problems such as incorrect stock quantities, duplicate product records, missed low-stock items, and mistakes while processing orders.

This project provides a simple solution by connecting the major parts of the workflow:

```text
Product Catalogue
       ↓
Inventory Management
       ↓
Customer Order
       ↓
Stock Validation
       ↓
Automatic Stock Deduction
       ↓
Order Processing
       ↓
Reports & Analytics
```

The project is intentionally designed using **only Python's built-in standard library**. No external Python packages, frameworks, databases, or APIs are required.

---

# 🎯 Project Objectives

The main objectives of the project are:

1. Manage an e-commerce product catalogue.
2. Maintain accurate inventory quantities.
3. Allow products to be added, updated, searched, and deleted.
4. Detect products that have reached their reorder level.
5. Create customer orders containing multiple products.
6. Automatically reduce inventory when an order is placed.
7. Prevent orders when sufficient stock is unavailable.
8. Manage the status of existing orders.
9. Restore inventory when an order is cancelled.
10. Generate useful inventory and sales reports.
11. Store application data persistently using JSON.
12. Demonstrate modular Python programming and object-oriented design.
13. Provide validation and error handling for incorrect input.
14. Provide automated tests for important business rules.

---

# ✨ Main Features

## 📦 1. Product Management

The system provides complete basic product management functionality.

Users can:

- Add new products
- View all products
- Update product information
- Delete products
- Search products
- Organize products by category
- Set product prices
- Set opening stock
- Configure reorder levels

Each product contains:

```text
Product ID
Product Name
Category
Price
Stock Quantity
Reorder Level
```

The system prevents duplicate product IDs and invalid product values.

---

## 📊 2. Inventory Management

Inventory is automatically connected with order processing.

The system can:

- Display current stock
- Restock products
- Detect low-stock products
- Calculate inventory value
- Prevent negative inventory
- Automatically deduct stock after an order
- Restore stock after order cancellation

### Low-stock logic

A product is considered low-stock when:

```text
Current Stock <= Reorder Level
```

This allows store staff to identify products that need replenishment.

---

## 🔎 3. Product Search

Products can be searched using:

- Product ID
- Product name
- Product category

For example:

```text
Search: keyboard
```

The system will display matching products.

---

## 🛍️ 4. Order Management

The application allows store staff to create customer orders containing one or more products.

An order contains:

```text
Order ID
Customer Name
Ordered Products
Quantity
Unit Price
Subtotal
Order Total
Order Status
```

When an order is successfully created, the corresponding inventory quantities are automatically reduced.

---

## 🧮 5. Automatic Order Total

Each order item calculates its own subtotal:

```text
Subtotal = Quantity × Unit Price
```

The complete order total is:

```text
Order Total = Sum of all Item Subtotals
```

The system displays monetary values in Indian Rupees.

Example:

```text
Wireless Mouse × 2 = ₹1,398.00
USB-C Cable    × 1 = ₹399.00

Order Total = ₹1,797.00
```

---

# 🚦 6. Stock Validation

Before an order is created, the system checks whether enough stock is available.

Example:

```text
Available stock: 5
Requested quantity: 7
```

The order is rejected because the requested quantity is greater than the available stock.

This prevents the inventory from becoming negative.

---

# 🔄 7. Order Status Management

Orders can have predefined statuses:

```text
Pending
Processing
Shipped
Delivered
Cancelled
```

The store operator can update an order's status from the menu.

If an order is cancelled, its ordered quantities are returned to inventory.

Example:

```text
Before cancellation:
Wireless Mouse stock = 8

Cancelled order:
Wireless Mouse × 2

After cancellation:
Wireless Mouse stock = 10
```

---

# 🚨 8. Low Stock Alerts

The system automatically identifies products that have reached or fallen below their reorder level.

Example:

```text
Product              Stock    Reorder Level
------------------------------------------------
Laptop Stand            2           3
Mechanical Keyboard     4           4
```

This provides a simple inventory replenishment mechanism.

---

# 📈 9. Business Dashboard

The dashboard provides a quick operational summary.

It displays information such as:

- Number of products
- Total units in inventory
- Total inventory value
- Number of low-stock products
- Number of active orders
- Units sold
- Recorded revenue
- Order status distribution

Example:

```text
Products in catalogue : 5
Units currently held  : 103
Inventory value       : ₹58,430.00
Low-stock products    : 2

Active orders         : 7
Units sold            : 21
Recorded revenue      : ₹19,845.00
```

---

# 🏆 10. Top-Selling Products

The reporting module analyzes completed/non-cancelled orders and calculates product sales.

The report provides:

```text
Product ID
Product Name
Units Sold
Revenue
```

Products are arranged according to units sold so that the operator can quickly understand which products are generating the most sales volume.

---

# 💾 11. Persistent Data Storage

The project uses a local JSON file instead of an external database.

Data is stored in:

```text
data/store.json
```

The storage contains:

```text
Products
Orders
Order Items
Order Status
Customer Information
```

When the application is started again, previously saved information can be loaded.

This keeps the project simple to install while still demonstrating persistent storage.

---

# 🧱 Project Architecture

The application follows a lightweight layered architecture.

```text
┌─────────────────────────────────────┐
│          User Interface             │
│              main.py                │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│           Service Layer             │
│ inventory.py │ orders.py │ reports  │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│            Domain Models            │
│ Product │ Order │ OrderItem         │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Persistence Layer           │
│             storage.py              │
│              JSON                   │
└─────────────────────────────────────┘
```

The separation of responsibilities makes the application easier to understand, test, maintain, and extend.

---

# 📁 Project Structure

```text
ECommerce_Inventory_Order_Management_System/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── validators.py
│   ├── inventory.py
│   ├── orders.py
│   ├── reports.py
│   ├── utils.py
│   └── main.py
│
├── data/
│   └── store.json
│
├── tests/
│   └── test_system.py
│
├── docs/
│   ├── architecture.md
│   └── diagrams.md
│
├── run.py
├── README.md
├── statement.md
└── .gitignore
```

---

# 🧩 Module Description

| File | Purpose |
|---|---|
| `models.py` | Defines Product, Order and OrderItem models |
| `storage.py` | Handles JSON data loading and saving |
| `validators.py` | Validates user input |
| `inventory.py` | Handles catalogue and inventory operations |
| `orders.py` | Handles order creation and order statuses |
| `reports.py` | Generates dashboard and sales information |
| `utils.py` | Provides console formatting helpers |
| `main.py` | Controls the interactive application |
| `run.py` | Application entry point |
| `test_system.py` | Automated unit tests |

---

# 🛠️ Technologies Used

The project intentionally uses only Python's standard library.

### Programming Language

```text
Python 3
```

### Standard Library Components

- `dataclasses`
- `json`
- `pathlib`
- `collections`
- `datetime`
- `typing`
- `unittest`

### No External Libraries

The project does **not** require:

- NumPy
- Pandas
- Flask
- Django
- Streamlit
- SQLAlchemy
- Matplotlib
- Any third-party package

This makes the project easy to run on a standard Python installation.

---

# 💻 Requirements

The only software requirement is:

```text
Python 3
```

No database server or external package installation is required.

---

# ▶️ Installation & Execution

## Step 1 — Download or Clone the Repository

Clone the project:

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd ECommerce_Inventory_Order_Management_System
```

---

## Step 2 — Run the Application

Run:

```bash
python run.py
```

On systems where `python` points to Python 2, use:

```bash
python3 run.py
```

---

# 🖥️ Application Menu

After launching the application, the following menu is available:

```text
══════════════════════════════════════════════════════════════════════

  E-Commerce Inventory & Order Management System

══════════════════════════════════════════════════════════════════════

1. View Inventory
2. Add Product
3. Update Product
4. Delete Product
5. Search Products
6. Restock Product
7. Low Stock Alerts
8. Create Order
9. View Orders
10. Update Order Status
11. Business Dashboard
12. Top-Selling Products
0. Exit
```

---

# 🧪 Testing

The project contains automated tests using Python's built-in `unittest` framework.

No testing package needs to be installed.

Run:

```bash
python -m unittest discover -s tests -v
```

The test suite checks important system operations including:

- Product creation
- Duplicate product prevention
- Order creation
- Automatic stock deduction
- Insufficient stock handling
- Order cancellation
- Stock restoration
- Low-stock detection
- JSON persistence
- Business reporting

The current project contains **8 automated tests**, all passing.

---

# 🔐 Validation & Error Handling

The system validates user input before performing operations.

Examples include:

### Empty values

```text
Product name cannot be empty.
```

### Invalid price

```text
Price must be greater than zero.
```

### Invalid quantity

```text
Quantity must be greater than zero.
```

### Negative stock

```text
Stock cannot be negative.
```

### Duplicate product

```text
A product with this ID already exists.
```

### Missing product

```text
Product 'P9999' was not found.
```

### Insufficient inventory

```text
Insufficient stock for Wireless Mouse.
Available: 3.
```

These checks help prevent invalid application states.

---

# 📐 Design Documentation

The `docs` directory contains additional design information.

## Architecture

`docs/architecture.md`

Contains:

- System architecture
- Module responsibilities
- Data structures
- Persistence design

## Diagrams

`docs/diagrams.md`

Contains:

- Use Case Diagram
- Workflow Diagram
- Class Diagram
- Sequence Diagram
- ER-style Storage Diagram

These diagrams explain how the major components interact.

---

# 🗃️ Data Design

## Product

A product contains:

```text
product_id
name
category
price
stock
reorder_level
```

## Order

An order contains:

```text
order_id
customer_name
items
status
total
```

## Order Item

An order item contains:

```text
product_id
product_name
quantity
unit_price
subtotal
```

The system calculates subtotal and order total rather than requiring the user to enter those values manually.

---

# ⚙️ Important Business Rules

The application follows several rules to maintain consistency.

### Rule 1 — Product IDs must be unique

Two products cannot use the same product ID.

### Rule 2 — Price must be positive

A product cannot have a zero or negative price.

### Rule 3 — Stock cannot be negative

Inventory quantities must always be zero or greater.

### Rule 4 — Orders require products

An empty order cannot be created.

### Rule 5 — Stock must be available

An order cannot be created when requested quantity exceeds available stock.

### Rule 6 — Creating an order reduces stock

Successful orders immediately deduct their quantities from inventory.

### Rule 7 — Cancelling an order restores stock

Cancelled order quantities are returned to inventory.

### Rule 8 — Historical products are protected

A product that appears in order history cannot simply be deleted, protecting historical order information.

---

# 🧠 Python Concepts Demonstrated

This project demonstrates several important Python programming concepts:

### Variables and Data Types

Used for product, order, quantity, price, and status information.

### Conditional Statements

Used for validation and business rules.

### Loops

Used for menus, product lists, order items, and reports.

### Functions

Used to separate reusable operations.

### Classes and Objects

Used for:

```text
Product
OrderItem
Order
InventoryManager
OrderManager
ReportManager
JSONStorage
```

### Dataclasses

Used to create clean domain models.

### Dictionaries

Used for fast lookup of products and orders.

### Lists

Used for collections of order items and search results.

### Exception Handling

Used to prevent invalid input from crashing the application.

### File Handling

Used to persist data through JSON.

### Unit Testing

Used to verify important business operations.

### Modular Programming

Different responsibilities are divided into separate Python files.

---

# 📊 Functional Requirements

The system provides the following major functional modules:

## Module 1 — Inventory Management

- Product CRUD
- Search
- Stock tracking
- Restocking
- Low-stock detection

## Module 2 — Order Management

- Order creation
- Multiple order items
- Stock validation
- Stock deduction
- Status management
- Cancellation and stock restoration

## Module 3 — Reporting & Analytics

- Inventory summary
- Inventory value
- Sales summary
- Order status summary
- Top-selling products
- Customer spending analysis

These modules provide a complete workflow for a small e-commerce back-office system.

---

# 📋 Non-Functional Requirements

## Performance

Common operations are performed in memory and are intended to respond immediately for a small-business dataset.

## Usability

The application provides a simple numbered command-line menu with clear prompts and error messages.

## Reliability

Successful changes are persisted to JSON so data can survive application restarts.

## Maintainability

Responsibilities are separated across multiple modules rather than placing all code inside one large Python file.

## Resource Efficiency

Only Python's standard library and a small local JSON file are required.

## Error Handling

Invalid input and business-rule violations are handled through validation and exceptions.

## Scalability

The service layer is separated from the interface, making it possible to replace the command-line interface with another interface in the future.

---

# 🚧 Current Scope

The current project focuses on the internal management side of an e-commerce business.

### Included

```text
✔ Product catalogue
✔ Inventory
✔ Stock alerts
✔ Restocking
✔ Customer orders
✔ Order statuses
✔ Order cancellation
✔ Reports
✔ JSON persistence
✔ Validation
✔ Testing
```

### Not Included

```text
✘ Online payment gateway
✘ Real shipping integration
✘ Customer login system
✘ Admin authentication
✘ Live online storefront
✘ External database server
✘ Real-time payment processing
```

These features can be introduced as future enhancements.

---

# 🚀 Future Enhancements

The project can be expanded in several directions.

## Database Integration

Replace JSON storage with SQLite or another database system.

## Authentication

Introduce:

- Admin login
- Inventory manager accounts
- Role-based access

## Supplier Management

Add supplier information and purchase orders.

## Barcode Support

Allow products to be identified through barcode scanners.

## Discounts & Taxes

Add:

- Coupons
- Product discounts
- GST/tax calculation
- Final payable amount

## CSV Import & Export

Allow inventory data to be imported and exported through CSV files.

## Web Interface

The current service layer could later be connected to a web interface.

## REST API

A future version could expose product and order operations through an API.

## Advanced Analytics

Future versions could include:

- Monthly sales reports
- Category-wise sales
- Revenue trends
- Inventory turnover
- Demand forecasting

---

# 🧪 Manual Testing Checklist

Before submitting the project, the following scenarios can be tested manually:

```text
[ ] Start the application
[ ] View inventory
[ ] Add a product
[ ] Try adding a duplicate product
[ ] Search for a product
[ ] Update product details
[ ] Restock a product
[ ] View low-stock products
[ ] Create an order
[ ] Create an order with multiple items
[ ] Try ordering more than available stock
[ ] View order history
[ ] Change an order status
[ ] Cancel an order
[ ] Verify stock is restored
[ ] View dashboard
[ ] View top-selling products
[ ] Restart application
[ ] Verify saved data
[ ] Run automated tests
```

---

# 📝 Project Statement

A separate `statement.md` file is included in the repository.

It contains:

- Problem statement
- Project scope
- Target users
- Objectives
- Functional requirements
- Non-functional requirements
- Expected outcome

This provides a concise academic summary of the project.

---

# 📚 Documentation

Additional project documentation is available in the `docs` folder:

```text
docs/
├── architecture.md
└── diagrams.md
```

These documents provide the architecture and design diagrams needed to understand the internal structure of the system.

---

# 🔄 Typical System Workflow

A normal order-processing workflow is:

```text
              ┌──────────────┐
              │ Start System │
              └──────┬───────┘
                     ↓
             ┌───────────────┐
             │ View Product  │
             │  Inventory    │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Create Order  │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Check Stock   │
             └───────┬───────┘
                     ↓
              ┌──────┴──────┐
              │             │
           Available      Not Available
              │             │
              ↓             ↓
        Deduct Stock    Show Error
              │
              ↓
        Save the Order
              │
              ↓
        Process Order
              │
              ↓
       Update Order Status
              │
              ↓
          Delivered
```

---

# 🎓 Academic Relevance

The project demonstrates practical application of programming concepts in a real-world scenario.

It covers:

- Problem identification
- Requirement analysis
- Modular design
- Object-oriented programming
- Data structures
- File handling
- Validation
- Exception handling
- Testing
- Documentation
- Version control readiness

The project is structured to support the VITyarthi **Build Your Own Project** submission requirements.

---

# 📦 GitHub Repository Setup

After placing the project on GitHub:

```bash
git init
git add .
git commit -m "Initial e-commerce inventory management system"
git branch -M main
git remote add origin <YOUR_REPOSITORY_URL>
git push -u origin main
```

After future changes:

```bash
git add .
git commit -m "Improve inventory and order management"
git push
```

---

# 👨‍💻 Author

**Project:** E-Commerce Inventory & Order Management System

**Language:** Python

**Project Type:** Academic / Educational

**Architecture:** Modular Layered Architecture

**Storage:** JSON

**Testing:** Python `unittest`

**External Dependencies:** None

---

# 📄 License

This project is intended for educational and academic use.

---

# ⭐ Project Summary

The **E-Commerce Inventory & Order Management System** provides a complete small-scale solution for managing products, stock, customer orders, and operational reports.

Its main strength is the synchronization between orders and inventory:

```text
Order Created
     ↓
Stock Checked
     ↓
Stock Deducted
     ↓
Order Saved
     ↓
Order Processed
     ↓
If Cancelled → Stock Restored
```

The project combines practical e-commerce requirements with core Python programming concepts while remaining lightweight, understandable, testable, and easy to run.
