import inflect

p = inflect.engine()

# LISTA DE NOMBRES
selected_names = []

# LOOP
while True:
    try:
        item = input("Name: ").title()
        selected_names.append(item)
    except (EOFError, KeyboardInterrupt):
        break

mylist = p.join(selected_names)

print(f"Adieu, adieu, to {mylist}")
