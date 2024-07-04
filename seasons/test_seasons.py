from datetime import date
import seasons

# Prueba para la función convert
def test_convert():
    assert seasons.convert("2000-03-24") == date(2000, 3, 24)
    assert seasons.convert("2000-10-25") == date(2000, 10, 25)
    assert seasons.convert("Hola") == "Invalid Date"




