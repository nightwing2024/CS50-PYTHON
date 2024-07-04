months_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        # Verificación de la entrada
        date = input("Inserta la fecha: ").strip().title()

        # Fecha con /
        if "/" in date:
            month, day, year = date.split("/")

        # Fecha con ,
        elif "," in date:
            month, day, year = date.split(" ")
            if month in months_list:
                month = months_list.index(month) + 1
                day = day.strip(",")
        else:
            continue

        # Verificación de fechas
        if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
            continue
        else:
            break
    except ValueError:
        continue

month = int(month)
day = int(day)

print(f"{year}-{month:02}-{day:02}")
