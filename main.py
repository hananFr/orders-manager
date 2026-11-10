import json

def read_file(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_file(path, data):
    try:
        with open(path, 'w') as f:
            json.dump(data,f, indent=2)
    except Exception as e:
        print(e.__dict__)

products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]




def get_valid_product(products):
    is_valid_product = False
    while not is_valid_product:
        product_id = input("product_id?\n")
        if product_id.isdigit():
            for product in products:
                if product["id"] == int(product_id):
                    is_valid_product=True
    return int(product_id)

def get_valid_quantity():
    is_valid_quantity=False
    while not is_valid_quantity:
        quantity = input("Quantity?\n")
        if quantity.isdigit() and int(quantity) > 0:
            is_valid_quantity = True
    return int(quantity)

def calculate_price_with_discount(price):
    if price < 300:
        return price
    if 300 <= price < 700:
        return price*0.95
    if 700 <= price < 1500:
        return price*0.9
    else:
        return price * 0.85

def calculate_total_price(items, products):
    total = 0
    for item in items:
        for product in products:
            if product["id"] == item["product_id"]:
                total += calculate_price_with_discount(product["price"]) * item["quantity"]
    return total



def create_order():
    orders = read_file('./data.json')
    ids = []
    items = []
    # Choose producs
    escape_from_items_menu=False
    while not escape_from_items_menu:
        product_id = get_valid_product(products)
        quantity = get_valid_quantity()
        items.append({"product_id": product_id,"quantity": quantity})

        escape = input("""
        If you want to escape press 0
        to proceed press on any another key
        """)
        if escape == "0":
            escape_from_items_menu=True
    
    total = calculate_total_price(items, products)
    for order in orders:
        ids.append(order["id"])
    order_id = max([0,*ids]) + 1

    
    
    return {
        "id": order_id,
        "items": items,
        "total_price": total,
        "status": "OPEN"
    }

def menu():
    escape = False
    while not escape:
        user_choice = input("""
        ========== ORDER MANAGER ==========
1. Create order
2. Show all orders
3. Find order by ID
4. Close order
5. Show sales report
0. Exit
Choose option:         
        """)
        if user_choice == "0":
            escape = True
        if user_choice == "1":
            print(create_order())

menu()

    

# print(type(read_file('./data.json')))