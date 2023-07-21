from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(0, 60, "CS50 Shirtificate", align ='C')
    pdf.image('shirtificate.png',0, 70)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(50, 150, txt=f'{name} took CS50')
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()