class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        status = "В наявності" if self.stock > 0 else "Немає в наявності"
        return f"{self.name} — {self.price} грн ({status}, залишилось: {self.stock} шт.)"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            if product.name in self.items:
                self.items[product.name]["quantity"] += quantity
            else:
                self.items[product.name] = {"product": product, "quantity": quantity}
            product.stock -= quantity
            print(f"Додано до кошика: {product.name} x{quantity}")
        else:
            print(f"Не вдалося додати {product.name}: недостатньо товару на складі (доступно: {product.stock}).")

    def remove_product(self, product_name, quantity=1):
        if product_name in self.items:
            current_qty = self.items[product_name]["quantity"]
            product = self.items[product_name]["product"]
            
            if quantity >= current_qty:
                product.stock += current_qty
                del self.items[product_name]
                print(f"Товар {product_name} повністю видалено з кошика.")
            else:
                self.items[product_name]["quantity"] -= quantity
                product.stock += quantity
                print(f"З кошика видалено {product_name} x{quantity}")
        else:
            print(f"Товару {product_name} немає в кошику.")

    def get_total_price(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
            return
        
        print("\n--- Ваш кошик ---")
        for item in self.items.values():
            prod = item["product"]
            qty = item["quantity"]
            print(f"- {prod.name}: {qty} шт. x {prod.price} грн = {prod.price * qty} грн")
        print(f"Загальна вартість: {self.get_total_price()} грн")
        print("-----------------")


if __name__ == "__main__":
    p1 = Product("Смартфон", 15000, 5)
    p2 = Product("Навушники", 3000, 10)
    p3 = Product("Чохол для телефону", 400, 2)

    print("Доступні товари:")
    print(p1)
    print(p2)
    print(p3)
    print()

    my_cart = Cart()

    my_cart.add_product(p1, 1)
    my_cart.add_product(p2, 2)
    my_cart.add_product(p3, 3) 

    my_cart.show_cart()

    my_cart.remove_product("Навушники", 1)

    my_cart.show_cart()
    
    print("\nСтан складу після покупок:")
    print(p1)
    print(p2)
    print(p3)