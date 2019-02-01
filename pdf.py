from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform, pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import grey, black, white, lightgrey
from reservations import get_single, Reservation
from date import Date

#LENGTH 595 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def create_registration_form(res_id):
    res = get_single(int(res_id))
    r = Reservation()
    r.values_to_model(res)
    c = canvas.Canvas('/var/www/html/assets/requestForm.pdf')

    c.setFont('Courier', 10)
    c.drawString(20, 815, "Meldeschein / Registration form")
    c.drawString(260, 815, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    form = c.acroForm

    c.drawString(20, 790, "Datum Anreise")
    form.textfield(name="dateFrom", tooltip="Datum Anreise", x=100, y=785, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=r.dateFrom, fontSize=14, height=20)
    c.drawString(300, 790, "Datum Abreise")
    form.textfield(name="dateTo", tooltip="Datum Abreise", x=390, y=785, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=r.dateTo, fontSize=14, height=20)
    c.drawString(20, 760, "Name")
    form.textfield(name="name", tooltip="Name", x=100, y=755, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value=r.name, fontSize=14, height=20)
    c.drawString(20, 730, "Straße, Nr")
    form.textfield(name="street", tooltip="Straße, Nr", x=100, y=725, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value=r.street + ' ' + r.houseNumber,
                   fontSize=14, height=20)
    c.drawString(20, 700, "PLZ, Ort")
    form.textfield(name="city", tooltip="PLZ, Ort", x=100, y=695, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=240, textColor=black, forceBorder=True, value=r.postalCode + ', ' + r.city,
                   fontSize=14, height=20)
    c.drawString(353, 700, "Land")
    form.textfield(name="country", tooltip="Land", x=390, y=695, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=r.country, fontSize=14, height=20)
    c.drawString(20, 670, "Passnummer")
    form.textfield(name="passport", tooltip="Passnummer", x=100, y=665, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value="", fontSize=14, height=20)
    c.drawString(270, 670, "Staatsangehörigkeit")
    form.textfield(name="nationality", tooltip="Staatsangehörigkeit", x=390, y=665, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=r.nationality.lower(), fontSize=14, height=20)
    c.drawString(20, 640, "Geburtsdatum")
    form.textfield(name="birthdate", tooltip="Geburtsdatum", x=100, y=635, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=190, textColor=black, forceBorder=True, value="", fontSize=14, height=20)
    c.drawString(311, 640, "Mitreisende")
    form.textfield(name="count", tooltip="Anzahl der Mitreisenden", x=390, y=635, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=str(r.count), fontSize=14, height=20)

    c.drawString(20, 590, "Unterschrift")
    form.textfield(name="signature", tooltip="Unterschrift", x=100, y=585, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value="", fontSize=14, height=20)

    form.checkbox(name="bill", tooltip="Rechnungsanschrift stimmt überein", x=20, y=535, borderStyle="inset",
                  borderColor=black, fillColor=white, textColor=black, forceBorder=True, checked=r.isSameAsNormal)
    c.drawString(50, 540, "Die Rechnungsanschrift stimmt mit der Privatanschrift überein")

    c.drawString(20, 510, "Firmenname")
    form.textfield(name="companyName", tooltip="Firmenname", x=100, y=505, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value=r.companyName, fontSize=14, height=20)
    c.drawString(20, 480, "Straße, Nr")
    form.textfield(name="street", tooltip="Straße, Nr", x=100, y=475, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=440, textColor=black, forceBorder=True, value=r.billStreet + " " + r.billHouseNumber,
                   fontSize=14, height=20)
    c.drawString(20, 450, "PLZ, Ort")
    form.textfield(name="city", tooltip="PLZ, Ort", x=100, y=445, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=240, textColor=black, forceBorder=True, value=r.billPostalCode + ", " + r.billCity,
                   fontSize=14, height=20)
    c.drawString(353, 450, "Land")
    form.textfield(name="country", tooltip="Land", x=390, y=445, borderStyle="inset", borderColor=black, fontName="Courier",
                   fillColor=white, width=150, textColor=black, forceBorder=True, value=r.billCountry, fontSize=14, height=20)
    c.save()


def create_invoice(res_id):
    res = get_single(int(res_id))
    r = Reservation()
    r.values_to_model(res)
    c = canvas.Canvas('/var/www/html/assets/requestInvoice.pdf')

    pdfmetrics.registerFont(TTFont('Calibri', "Calibri.ttf"))
    pdfmetrics.registerFont(TTFont('CalibriBold', "CALIBRIB.TTF"))

    form = c.acroForm
    c.setFont("CalibriBold", 14)
    c.drawString(58, 800, "Ferienwohnung Grimm")
    c.setFont("Calibri", 11)
    c.drawString(58, 785, "Ferienwohnung - Monteurwohnung")

    c.setFont("CalibriBold", 11)
    c.drawRightString(538, 800, "Ferienwohnung Grimm")
    c.setFont("Calibri", 11)
    c.drawRightString(538, 788, "Elke und Peter Grimm")
    c.drawRightString(538, 776, "Mühlstraße 4")
    c.drawRightString(538, 764, "63579 Freigericht")
    c.drawRightString(538, 752, "+49 6055-6302")
    c.drawRightString(538, 740, "info@fewogrimm.de")
    c.drawRightString(538, 728, "www.fewogrimm.de")

    c.setFont('CalibriBold', 11)
    c.drawString(58, 716, "Rechnungsadresse")
    c.setFont("Calibri", 11)
    c.drawRightString(58, 704, r.companyName)
    c.drawRightString(58, 692, r.billStreet + " " + r.billHouseNumber)
    c.drawRightString(58, 680, r.billPostalCode + " " + r.billCity)
    c.drawRightString(58, 668, r.billCountry)

    c.setFont('CalibriBold', 13)
    c.drawString(58, 615, "Rechnung")
    c.setFont('CalibriBold', 11)
    c.drawString(58, 590, "Rechnungsnummer")
    c.setFont('Calibri', 11)
    c.drawString(178, 590, "1")
    c.setFont('CalibriBold', 11)
    c.drawString(358, 590, "Datum")
    c.setFont('Calibri', 11)
    c.drawString(458, 590, Date.get_current())
    c.setFont('CalibriBold', 11)
    c.drawString(58, 575, "Anreise")
    c.setFont('Calibri', 11)
    c.drawString(178, 575, r.dateFrom)
    c.setFont('CalibriBold', 11)
    c.drawString(358, 575, "Abreise")
    c.setFont('Calibri', 11)
    c.drawString(458, 575, r.dateTo)
    c.setFont('CalibriBold', 11)
    c.drawString(58, 560, "Gastname")
    c.setFont('Calibri', 11)
    c.drawString(178, 560, r.name)
    c.setFont('CalibriBold', 11)
    c.drawString(358, 560, "Personenzahl")
    c.setFont('Calibri', 11)
    c.drawString(458, 560, str(r.count))

    c.line(58, 520, 538, 520) #58 Startwert = +38
    c.line(58, 520, 58, 445)
    c.line(58, 445, 538, 445)
    c.line(538, 445, 538, 520)
    c.line(58, 490, 538, 490)
    c.line(188, 520, 188, 445)
    c.line(438, 520, 438, 445)

    c.setFont('CalibriBold', 11)
    c.drawString(68, 500, "Anzahl")
    c.drawString(198, 500, "Beschreibung")
    c.drawString(448, 500, "Preis")

    date_from = Date()
    date_from.string_to_model(r.dateFrom)
    date_to = Date()
    date_to.string_to_model(r.dateTo)
    duration = date_from.get_duration(date_to)

    c.setFont('Calibri', 11)
    c.drawString(68, 470, str(duration) + " Tage")

    c.drawString(198, 470, "Ferienwohnung - Gartenstraße 17")
    c.drawString(198, 455, "2,5 Zimmer, Küche, Bad")
    c.drawString(448, 470, r.price + "€")

    c.save()