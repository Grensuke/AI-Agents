# dicts and json

MENU = {"plum cake": 500, "chocolate cake": 650, "cupcake": 80}   # key → value

MENU["plum cake"]                  # 500
MENU.get("donut", "not on menu")   # 'not on menu'  (no crash)
# MENU["donut"]                      # KeyError: 'donut'  (crash!)

order = {"name": "Ravi", "item": "plum cake", "qty": 2, "eggless": True}
order["qty"] * MENU[order["item"]] # 1000

import json
text = json.dumps(order)           # dict → JSON string, to send or save
back = json.loads(text)            # JSON string → dict

print(text)
print(back)

def get_price(item: str, qty: int = 1):
    """Return the total price in rupees for qty of an item on the Sweet Crumbs menu."""
    return MENU[item.lower().strip()] * qty

print(get_price("Cupcake ", 7))
