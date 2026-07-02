# =====================================
# INVENTORY MANAGEMENT SYSTEM
# FAC Academy - Complete Version
# =====================================

# --- Sample inventory data (list of dicts) ---
inventory = [
    {"id": "P001", "name": "Laptop",     "category": "Electronics", "price": 85000.00, "qty": 15},
    {"id": "P002", "name": "Mouse",      "category": "Electronics", "price":  1200.00, "qty":  8},
    {"id": "P003", "name": "Desk Chair", "category": "Furniture",   "price": 12500.00, "qty":  5},
    {"id": "P004", "name": "Notebook",   "category": "Stationery",  "price":   150.00, "qty": 50},
    {"id": "P005", "name": "USB Cable",  "category": "Electronics", "price":   500.00, "qty":  3},
]


# --- Helper: generate next product ID ---
def generate_id():
    if not inventory:
        return "P001"
    last_id = max(int(p["id"][1:]) for p in inventory)
    return f"P{last_id + 1:03d}"


# =====================================
# FEATURE 1: Add New Product
# =====================================
def add_product():
    print("\n--- ADD NEW PRODUCT ---")
    name     = input("Product Name : ").strip().title()
    category = input("Category     : ").strip().title()
    price    = float(input("Price (KES)  : "))
    qty      = int(input("Quantity     : "))

    product = {
        "id":       generate_id(),
        "name":     name,
        "category": category,
        "price":    price,
        "qty":      qty,
    }
    inventory.append(product)
    print(f"\nProduct '{name}' added successfully with ID {product['id']}.")


# =====================================
# FEATURE 2: Display All Inventory
# =====================================
def display_inventory():
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n" + "=" * 72)
    print(f"{'ID':<8} {'NAME':<20} {'CATEGORY':<15} {'PRICE (KES)':>12} {'QTY':>6}")
    print("-" * 72)
    for p in inventory:
        print(f"{p['id']:<8} {p['name']:<20} {p['category']:<15} {p['price']:>12,.2f} {p['qty']:>6}")
    print("=" * 72)
    print(f"Total products in inventory: {len(inventory)}")


# =====================================
# FEATURE 3: Search Product by Name
# =====================================
def search_product():
    print("\n--- SEARCH PRODUCT ---")
    keyword = input("Enter product name to search: ").strip().lower()
    results = [p for p in inventory if keyword in p["name"].lower()]

    if not results:
        print(f"No products found matching '{keyword}'.")
    else:
        print(f"\n{len(results)} result(s) found:")
        print("-" * 55)
        for p in results:
            print(f"  ID       : {p['id']}")
            print(f"  Name     : {p['name']}")
            print(f"  Category : {p['category']}")
            print(f"  Price    : KES {p['price']:,.2f}")
            print(f"  Quantity : {p['qty']}")
            print("-" * 55)


# =====================================
# FEATURE 4: Update Product Price or Quantity
# =====================================
def update_product():
    print("\n--- UPDATE PRODUCT ---")
    product_id = input("Enter product ID to update: ").strip().upper()
    product    = next((p for p in inventory if p["id"] == product_id), None)

    if not product:
        print(f"Product with ID '{product_id}' not found.")
        return

    print(f"\nProduct found: {product['name']}")
    print("What would you like to update?")
    print("  1. Price")
    print("  2. Quantity")
    print("  3. Both")
    choice = input("Choice (1/2/3): ").strip()

    if choice in ("1", "3"):
        new_price       = float(input(f"New price (current: KES {product['price']:,.2f}): "))
        product["price"] = new_price

    if choice in ("2", "3"):
        new_qty        = int(input(f"New quantity (current: {product['qty']}): "))
        product["qty"] = new_qty

    if choice in ("1", "2", "3"):
        print(f"\nProduct '{product['name']}' updated successfully.")
    else:
        print("Invalid choice. No changes made.")


# =====================================
# FEATURE 5: Delete a Product
# =====================================
def delete_product():
    print("\n--- DELETE PRODUCT ---")
    product_id = input("Enter product ID to delete: ").strip().upper()
    product    = next((p for p in inventory if p["id"] == product_id), None)

    if not product:
        print(f"Product with ID '{product_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete '{product['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        inventory.remove(product)
        print(f"Product '{product['name']}' deleted successfully.")
    else:
        print("Deletion cancelled.")


# =====================================
# FEATURE 6: Low Stock Alert
# =====================================
def low_stock_alert(threshold=10):
    print(f"\n--- LOW STOCK ALERT (Qty < {threshold}) ---")
    low_stock = [p for p in inventory if p["qty"] < threshold]

    if not low_stock:
        print("All products are sufficiently stocked.")
    else:
        print(f"{len(low_stock)} product(s) need restocking:\n")
        print(f"{'ID':<8} {'NAME':<20} {'CATEGORY':<15} {'QTY':>6}")
        print("-" * 55)
        for p in low_stock:
            print(f"{p['id']:<8} {p['name']:<20} {p['category']:<15} {p['qty']:>6}  -- RESTOCK NEEDED")
        print("-" * 55)


# =====================================
# FEATURE 7: Total Inventory Value
# =====================================
def total_inventory_value():
    print("\n--- TOTAL INVENTORY VALUE ---")
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"\n{'NAME':<20} {'PRICE (KES)':>12} {'QTY':>6} {'VALUE (KES)':>14}")
    print("-" * 58)
    grand_total = 0
    for p in inventory:
        value        = p["price"] * p["qty"]
        grand_total += value
        print(f"{p['name']:<20} {p['price']:>12,.2f} {p['qty']:>6} {value:>14,.2f}")

    print("=" * 58)
    print(f"{'GRAND TOTAL INVENTORY VALUE':<40} KES {grand_total:>10,.2f}")
    print("=" * 58)


# =====================================
# MAIN MENU
# =====================================
def main():
    while True:
        print("\n" + "=" * 42)
        print("      INVENTORY MANAGEMENT SYSTEM")
        print("=" * 42)
        print("  1. Add New Product")
        print("  2. Display All Inventory")
        print("  3. Search Product by Name")
        print("  4. Update Product Price / Quantity")
        print("  5. Delete a Product")
        print("  6. Low Stock Alert")
        print("  7. Total Inventory Value")
        print("  0. Exit")
        print("=" * 42)

        choice = input("Select option: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            low_stock_alert()
        elif choice == "7":
            total_inventory_value()
        elif choice == "0":
            print("\nExiting system. Goodbye.")
            break
        else:
            print("Invalid option. Please choose between 0 and 7.")


if __name__ == "__main__":
    main()