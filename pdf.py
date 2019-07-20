from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform, pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import grey, black, white, lightgrey
from reservations import get_single, Reservation, set_invoice_number
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
    c.drawString(40, 815, "Meldeschein / registration form")
    c.setFont("Calibri", 11)
    c.drawRightString(555, 815, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    form = c.acroForm

    c.line(40, 804, 555, 804)
    c.setFont('CalibriBold', 11)
    c.drawString(50, 780, "Privatanschrift / home address")
    c.drawString(220, 780, "Datum Anreise /")
    c.drawString(220, 770, "date of arrival")
    c.setFont("Calibri", 11)
    c.drawString(320, 780, r.dateFrom)
    c.setFont('CalibriBold', 11)
    c.drawString(397, 780, "Datum Abreise /")
    c.drawString(397, 770, "date of departure")
    c.setFont("Calibri", 11)
    c.drawString(497, 780, r.dateTo)
    c.line(40, 754, 555, 754)
    c.drawString(50, 740, "Name / name")
    c.drawString(220, 740, r.name)
    c.line(40, 734, 555, 734)
    c.drawString(50, 720, "Straße, Nr. / street")
    c.drawString(220, 720, r.street + " " + r.houseNumber)
    c.line(40, 714, 555, 714)
    c.drawString(50, 700, "PLZ, Ort / postal code, city")
    c.drawString(220, 700, r.postalCode + " " + r.city)
    c.drawString(397, 700, "Land / country")
    c.drawString(494, 700, r.country)
    c.line(40, 694, 555, 694)
    c.drawString(50, 680, "Staatsangehörigkeit / nationality")
    c.drawString(220, 680, r.nationality)
    c.drawString(330, 680, "Passnummer / passport number")
    c.drawString(497, 680, "")
    c.line(40, 674, 555, 674)
    c.drawString(50, 660, "Geburtsdatum / date of birth")
    c.drawString(220, 660, "")
    c.drawString(330, 660, "Anzahl der Mitreisenden /")
    c.drawString(330, 650, "number of accompanying persons")
    c.drawString(494, 660, str(r.count - 1))
    c.line(40, 644, 555, 644)
    c.line(40, 804, 40, 644)
    c.line(555, 804, 555, 644)
    c.line(210, 804, 210, 644)
    c.line(387, 804, 387, 754)
    c.line(387, 714, 387, 694)
    c.line(487, 714, 487, 644)
    c.line(320, 694, 320, 644)

    c.line(40, 610, 555, 610)
    c.line(40, 580, 555, 580)
    c.line(40, 610, 40, 580)
    c.line(555, 610, 555, 580)
    c.drawString(50, 590, "Unterschrift des Gastes / signature")

    c.line(40, 560, 555, 560)
    c.setFont("CalibriBold", 11)
    c.drawString(50, 540, "Rechnungsanschrift /")
    c.drawString(50, 530, "billing address.")
    c.drawString(220, 540, "Die Privatanschrift stimmt mit der Rechnungsanschrift überein. /")
    c.drawString(220, 530, "The home address matches the billing address.")
    c.setFont("Calibri", 11)
    if r.isSameAsNormal:
        c.drawString(530, 535, "JA")
    else:
        c.drawString(530, 535, "NEIN")
    c.line(40, 514, 555, 514)
    c.drawString(50, 500, "Firma / company")
    if not r.isSameAsNormal:
        c.drawString(220, 500, r.companyName)
    c.line(40, 494, 555, 494)
    c.drawString(50, 480, "Firmenadresse / company address")
    if not r.isSameAsNormal:
        c.drawString(220, 480, r.billStreet + " " + r.billHouseNumber + " | " + r.billPostalCode + " " + r.billCity + " | " + r.billCountry)
    c.line(40, 474, 555, 474)
    c.line(210, 560, 210, 474)
    c.line(40, 560, 40, 474)
    c.line(555, 560, 555, 474)

    c.save()


def create_invoice(res_id):
    res = get_single(int(res_id))
    r = Reservation()
    r.values_to_model(res)

    if r.invoiceType == "default" or r.invoiceType == "booking":
        if r.invoiceNumber == -1:
            file = open("invoice.number", "r")
            r.invoiceNumber = int(file.read()) + 1
            file.close()
            file = open("invoice.number", "w")
            file.write(str(r.invoiceNumber))
            file.close()
            set_invoice_number(res_id, r.invoiceNumber)


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
    c.drawString(68, 470, str(duration) + " Übernachtungen")

    c.drawString(198, 470, "Ferienwohnung - Gartenstraße 17")
    c.drawString(198, 455, "2,5 Zimmer, Küche, Bad")
    c.drawString(448, 470, r.price + "€")

    c.drawString(58, 418,
                 "Kein Ausweis der Umsatzsteuer aufgrund der Anwendung der Kleinunternehmerregelung (§ 19 UStG).")
    if r.invoiceType == 'booking':
        c.drawString(58, 398, "Abrechnung und Bezahlung via booking.com")
    c.drawString(58, 378, "Wir danken recht herzlich für ihren Besuch und wünschen Ihnen eine angenehme Heimreise.")

    c.drawCentredString(289, 66, "Ferienwohnung Grimm | Mühlstraße 4 | 63579 Freigericht")
    c.drawCentredString(289, 54, "+49 6055-6302 | info@fewogrimm.de | www.fewogrimm.de")
    c.drawCentredString(289, 42, "VR-Bank MKB eG | IBAN: DE54 5066 1639 0200 8720 32 | BIC: GENODEF1LSR")

    c.save()