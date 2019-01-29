from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import grey, black, white


def create_simple_form():
    c = canvas.Canvas('test.pdf')

    c.setFont('Courier', 10)
    c.drawString(10, 825, "Meldeschein / Registration form")
    c.drawString(260, 825, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    form = c.acroForm

    c.drawString(10, 790, "Datum Anreise")
    form.textfield(name="dateFrom", tooltip="Datum Anreise", x=100, y=785, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(300, 790, "Datum Abreise")
    form.textfield(name="dateTo", tooltip="Datum Abreise", x=390, y=785, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 760, "Name, Vorname")
    form.textfield(name="name", tooltip="Name, Vorname", x=100, y=755, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 730, "Straße, Nr")
    form.textfield(name="street", tooltip="Straße, Nr", x=100, y=725, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 700, "PLZ, Ort")
    form.textfield(name="city", tooltip="PLZ, Ort", x=100, y=695, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=240, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(353, 700, "Land")
    form.textfield(name="country", tooltip="Land", x=390, y=695, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 670, "Passnummer")
    form.textfield(name="passport", tooltip="Passnummer", x=100, y=665, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="", fontSize=14, height=20)
    c.drawString(270, 670, "Staatsangehörigkeit")
    form.textfield(name="nationality", tooltip="Staatsangehörigkeit", x=390, y=665, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 640, "Geburtsdatum")
    form.textfield(name="birthdate", tooltip="Geburtsdatum", x=100, y=635, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=190, textColor=black, forceBorder=True, value="", fontSize=14, height=20)
    c.drawString(311, 640, "Mitreisende")
    form.textfield(name="count", tooltip="Anzahl der Mitreisenden", x=390, y=635, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)

    c.drawString(10, 590, "Unterschrift")
    form.textfield(name="signature", tooltip="Unterschrift", x=100, y=585, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="", fontSize=14, height=20)

    form.checkbox(name="bill", tooltip="Rechnungsanschrift stimmt überein", x=10, y=535, borderStyle="inset",
                  borderColor=black, fillColor=white, textColor=black, forceBorder=True)
    c.drawString(40, 540, "Die Rechnungsanschrift stimmt mit der Privatanschrift überein")

    c.drawString(10, 510, "Firmenname")
    form.textfield(name="companyName", tooltip="Firmenname", x=100, y=505, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 480, "Straße, Nr")
    form.textfield(name="street", tooltip="Straße, Nr", x=100, y=475, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(10, 450, "PLZ, Ort")
    form.textfield(name="city", tooltip="PLZ, Ort", x=100, y=445, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=240, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.drawString(353, 450, "Land")
    form.textfield(name="country", tooltip="Land", x=390, y=445, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="hallo", fontSize=14, height=20)
    c.save()

create_simple_form()