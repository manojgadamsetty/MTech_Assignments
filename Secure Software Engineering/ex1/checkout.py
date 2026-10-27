BITS_ID = "2025MT12100"
SERVER_PRICE = 55000


def checkout(server_price, qty, client_price):
    if isinstance(qty, bool) or not isinstance(qty, int) or not 1 <= qty <= 10:
        raise ValueError("Quantity must be a whole number from 1 to 10.")
    return {"qty": qty, "total": server_price * qty}


print(BITS_ID)
for quantity in [1, 0, 11, -2, 2.5]:
    try:
        print(quantity, "->", checkout(SERVER_PRICE, quantity, 1))
    except ValueError as error:
        print(quantity, "-> rejected:", error)
