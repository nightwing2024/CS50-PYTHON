from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", size=20)

ask = input("What's Your Name?: ")

pdf.cell(200, 10, txt="CS50 Shirtificate", ln=True, align="C")

pagina_ancho = pdf.w
imagen_ancho = 150
pos_x = (pagina_ancho - imagen_ancho) / 2

pdf.image(
    "shirtificate.png",
    x=pos_x,
    y=60,
    w=150,
    h=150,
)

texto_ancho = pdf.get_string_width(ask)
pos_texto_x = pos_x + (imagen_ancho - texto_ancho) / 2
pos_texto_y = 60 + 150 / 2

pdf.text(pos_texto_x, pos_texto_y, ask)

pdf.output("shirtificate.pdf")
