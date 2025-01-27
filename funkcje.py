shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor",
    ]
shopping_items.extend([
        "mleko",
        "czekolada",
])
payment = "cart"
shop= "local"
def shopping(items, payment, shop):
    shopping_cart = "Twój koszyk zawiera:\n "
    for item in items:  
      shopping_cart += item + "\n "
    shopping_cart += "Sposób płatności: " + payment + "\n"
    shopping_cart += "Sklep: " + shop + "\n"
    return shopping_cart
basket = shopping(shopping_items, payment, shop= "local")
print(basket)