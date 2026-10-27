BITS_ID = "2025MT12100"


def checkout(server_price, qty, client_price):
    total = client_price * qty
    return {"qty": qty, "total": total}


print(BITS_ID)
print(checkout(55000, -2, 1))
