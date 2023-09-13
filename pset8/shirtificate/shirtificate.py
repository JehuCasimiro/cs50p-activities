from fpdf import FPDF

class PDF(FPDF):
    def create(self, name):
        # title
        self.add_page()
        self.set_font('Helvetica', 'B', 50)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.w - 20)

        # name
        self.set_font('Helvetica', '', 25)
        self.set_text_color(255, 255, 255)
        self.text(x=55, y=140, txt=f"{name} took CS50")



    def save(self, file):
        self.output(file)


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.create(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
