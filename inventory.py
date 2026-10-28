def merge_inventory(*stores):
    combined_stock = {}
    for store in stores:
        for product, quantity in store.items():
            combined_stock[product] = combined_stock.get(product, 0) + quantity
    return combined_stock

def show_inventory(stock_data):
    print("\nInventory Details:")
    for product, quantity in stock_data.items():
        print(product, ":", quantity)

def query_stock(stock_data):
    product_name = input("\nEnter item name to check: ").strip()
    if product_name in stock_data:
        print("Available Quantity:", stock_data.get(product_name, 0))
    else:
        print("Item not found.")

branch_a = {"Pen": 20, "Book": 15, "Pencil": 30}
branch_b = {"Pen": 10, "Book": 25, "Eraser": 12}
branch_c = {"Pencil": 15, "Eraser": 8}

total_inventory = merge_inventory(branch_a, branch_b, branch_c)
show_inventory(total_inventory)

updated_stock = {item: count for item, count in total_inventory.items()}

restock_batch = {"Pen": 5, "Marker": 10}
for item, count in restock_batch.items():
    updated_stock[item] = updated_stock.get(item, 0) + count

print("\nUpdated Inventory:")
show_inventory(updated_stock)

query_stock(updated_stock)
