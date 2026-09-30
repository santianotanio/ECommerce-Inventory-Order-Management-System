# Project Statement

## Project Title
**E-Commerce Inventory & Order Management System**

## Problem Statement
Small e-commerce businesses need to keep product information, stock quantities and customer orders synchronized. Manual tracking can cause duplicate product records, incorrect stock counts, missed low-stock items and order-processing mistakes.

This project provides a lightweight command-line system that centralizes catalogue management, inventory tracking, order processing and business reporting in one application.

## Scope
The project covers:
1. Product catalogue management.
2. Stock monitoring and restocking.
3. Customer order creation.
4. Order-status management.
5. Automatic stock deduction and restoration.
6. Low-stock alerts.
7. Basic operational analytics.
8. Local persistent storage.

The project does not include payment gateways, real shipping APIs, authentication servers or an online storefront.

## Target Users
- Small online-store owners
- Inventory managers
- Order-processing staff
- Students learning Python application development

## Objectives
- Reduce manual inventory errors.
- Keep order and stock information synchronized.
- Provide a clear CRUD workflow.
- Provide useful operational reports.
- Demonstrate modular Python programming.
- Build the solution without external libraries.

## Functional Requirements

### FR1 — Product Management
The user shall be able to add, view, update, search and delete products.

### FR2 — Inventory Management
The system shall maintain stock quantities and allow authorized stock increases through restocking.

### FR3 — Low-Stock Monitoring
The system shall identify products whose stock is at or below the configured reorder level.

### FR4 — Order Creation
The system shall create orders containing one or more products and quantities.

### FR5 — Stock Synchronization
The system shall reduce stock when an order is created.

### FR6 — Order Status
The system shall allow order statuses to be updated through predefined states.

### FR7 — Cancellation
The system shall return ordered quantities to inventory when an order is cancelled.

### FR8 — Reporting
The system shall display inventory and sales summaries and identify top-selling products.

### FR9 — Persistence
The system shall save products and orders to a local JSON file.

### FR10 — Validation
The system shall reject invalid IDs, empty names, non-positive prices, negative stock and insufficient inventory.

## Non-Functional Requirements

### Performance
For the intended small-business dataset, common catalogue and order operations should complete immediately from local memory.

### Usability
The menu-driven interface should provide clear choices, readable tables and understandable error messages.

### Reliability
Data should be persisted after successful changes so that the application can resume from its previous state.

### Maintainability
Business responsibilities are divided across models, storage, validation, inventory, orders, reports and UI modules.

### Resource Efficiency
The system uses only Python standard-library components and local JSON storage, avoiding external services and package dependencies.

### Error Handling
Invalid user input and business-rule violations are caught and reported without terminating the application.

### Scalability
The business logic is separated from the presentation layer so a future web or database interface can reuse the core services.

## Expected Outcome
A working Python application that demonstrates a complete e-commerce back-office workflow while remaining simple enough to understand, test and extend.
