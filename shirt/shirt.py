from PIL import Image, ImageOps
import sys
import os


def main():
    check_argv()
    # Abre la imagen de la marioneta
    original = Image.open(sys.argv[1])

    # Abre la imagen de la camiseta y ajusta su tamaño
    shirt = Image.open("shirt.png")

    original = ImageOps.fit(original, (600, 600))

    # Superpone la imagen de la camiseta en la imagen de la marioneta
    original.paste(shirt, shirt)

    # Guarda la imagen resultante
    original.save(sys.argv[2])


def check_argv():
    if len(sys.argv) == 3:
        path = sys.argv[2]
        extension = os.path.splitext(path)
        if extension[1] not in sys.argv[1] and sys.argv[2]:
            sys.exit("Input and output have different extensions")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
