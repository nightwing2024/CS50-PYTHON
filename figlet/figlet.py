import sys
import random
from pyfiglet import Figlet

# Crear una instancia de Figlet
figlet = Figlet()


# Obtener la lista de fuentes disponibles
available_fonts = figlet.getFonts()

# Seleccionar una fuente aleatoria
selected_font = random.choice(available_fonts)

# Configurar la fuente del texto
figlet.setFont(font=selected_font)

if len(sys.argv) == 1:
    ask = input("Input:")
    art = figlet.renderText(ask)
    print("Output:", art)

elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        font_name = sys.argv[2]
        if font_name in available_fonts:
            figlet.setFont(font=font_name)
            ask = input("Input:")
            art = figlet.renderText(ask)
            print(art)
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
