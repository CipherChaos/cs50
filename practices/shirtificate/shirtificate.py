from fpdf import FPDF


class PDF(FPDF):
    def header(self):

        self.set_font("helvetica", "", 30)

        title = "CS50 Shirtificate"
        title_w = self.get_string_width(title)
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)

        self.cell(title_w, 20, title, 0, 1, 'C')

        self.ln(20)


def main():
    name = input("Name: ")


    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")


    pdf.image("shirtificate.png", x=10, y=70, w=190)


    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)


    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", 0, 1, 'C')

    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()