from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform, pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import grey, black, white, lightgrey
from reservations import get_single, Reservation
from date import Date

# 595 * 842 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def make_nice(text):
    text = text.replace("Ä", "Ae")
    text = text.replace("ä", "ae")
    text = text.replace("Ö", "Oe")
    text = text.replace("ö", "oe")
    text = text.replace("Ü", "Ue")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")
    return text


def create_registration_form(res_id):
    res = get_single(int(res_id))
    r = Reservation()
    r.values_to_model(res)
    c = canvas.Canvas('/var/www/html/assets/requestForm.pdf')

    pdfmetrics.registerFont(TTFont('Calibri', "Calibri.ttf"))
    pdfmetrics.registerFont(TTFont('CalibriBold', "CALIBRIB.TTF"))

    c.setFont('CalibriBold', 11)
    c.drawString(40, 815, "Meldeschein / Registration form")
    c.setFont("Calibri", 11)
    c.drawRightString(555, 815, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    form = c.acroForm

    c.line(40, 800, 555, 800)
    c.setFont('CalibriBold', 11)
    c.drawString(50, 780, "Privatanschrift / Home address")
    c.drawString(200, 780, "Datum Anreise /")
    c.drawString(200, 770, "Date of arrival")
    c.drawString(300, 780, r.dateFrom)
    c.drawString(377, 780, "Datum Abreise /")
    c.drawString(377, 770, "Date of departure")
    c.drawString(477, 780, r.dateFrom)
    c.line(40, 750, 555, 750)
    c.save()


def create_invoice(res_id):
    res = get_single(int(res_id))
    r = Reservation()
    r.values_to_model(res)

    if r.invoiceType == "default":
        if r.invoiceNumber == -1:
            file = open("invoice.number", "r")
            r.invoiceNumber = int(file.read()) + 1
            file.close()
            file = open("invoice.number", "w")
            file.write(str(r.invoiceNumber))
            file.close()

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
    c.drawString(58, 704, r.companyName)
    c.drawString(58, 692, r.billStreet + " " + r.billHouseNumber)
    c.drawString(58, 680, r.billPostalCode + " " + r.billCity)
    c.drawString(58, 668, r.billCountry)

    c.setFont('CalibriBold', 13)
    c.drawString(58, 615, "Rechnung")
    c.setFont('CalibriBold', 11)
    c.drawString(58, 590, "Rechnungsnummer")
    c.setFont('Calibri', 11)
    c.drawString(178, 590, str(r.invoiceNumber))
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

    c.drawString(58, 418,
                 "Kein Ausweis der Umsatzsteuer aufgrund der Anwendung der Kleinunternehmerregelung (§ 19 UStG).")
    c.drawString(58, 388, "Wir danken recht herzlich für ihren Besuch und wünschen Ihnen eine angenehme Heimreise.")

    c.drawCentredString(289, 66, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    c.drawCentredString(289, 54, "+49 6055-6302 | info@fewogrimm.de | www.fewogrimm.de")
    c.drawCentredString(289, 42, "VR-Bank MKB eG | IBAN: DE54 5066 1639 0200 8720 32 | BIC: GENODEF1LSR")

    c.save()