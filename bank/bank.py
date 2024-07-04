
#
main = input(": ").strip()

#
main_lower = main.lower()

#
if main_lower.startswith("hello"):
    value = 0
elif main_lower.startswith("h"):
    value = 20
else:
    value = 100

#
print(f"${value}")
