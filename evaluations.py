from pizza import Pizza

print(f"Ingrediente Proteico Seleccionado: {Pizza.proteic}")
print(f"Vegetal 1 Seleccionado: {Pizza.vegetable1}")
print(f"Vegetal 2 Seleccionado: {Pizza.vegetable2}")
print(f"Tipo de Masa Seleccionado: {Pizza.type_dough}")
print(f"Su pizza es: {Pizza.validate}")

print("\nValidar si Salsa Tomate existe")
print(Pizza.elementValidate("Salsa Tomate", ["Salsa Tomate", "Salsa BBQ"]))

print("\nHora de hacer un pedido!")
my_pizza = Pizza()
my_pizza.placeOrder()

print("\nEl detalles del pedido es:")
print(f"Su Proteico es: {my_pizza.proteic}")
print(f"Su Vegetal 1 es: {my_pizza.vegetable1}")
print(f"Su Vegetal 2 es: {my_pizza.vegetable2}")
print(f"La Masa es de tipo: {my_pizza.type_dough}")
print(f"Su pedido ha sido: {my_pizza.validate}")


print("\nRevisemos si el validador funciona")
print(Pizza.validate)