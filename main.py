import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains bill details like total amount and time period of bill
    """

    # class is a blueprint of objects.
    def __init__(self, amount, period):
        # object instance made by the Object class
        # shortcut is ALT + Enter
        self.amount = amount
        self.period = period


class Roommate:
    """
    Object of the roommate that pays some of the bills
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    # what does the roommate do> - Pays!

    def pays_bill(self, bill, roommate2):
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PDF_Reader:
    """
    Creates PDF report of month and generate report for roommates, with names and due amount and period of stay
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, roommate1, roommate2, bill):
        roommate1_pay = str(round(roommate1.pays_bill(bill=bill, roommate2=roommate2), 2))
        roommate2_pay = str(round(roommate2.pays_bill(bill=bill, roommate2=roommate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert Photo/Icon
        pdf.image(name="house_icon.png", w=100, h=100)

        # Insert Title
        pdf.set_font(family='Arial', size=30, style='B')
        # Insertion of period label
        pdf.set_font(family="Times", size=14, style="I")
        pdf.cell(w=0, h=80, txt="Roommate Monthly Bill", border=0, align="C", ln=1)
        # Insertion of period and month
        pdf.set_font(family="Helvetica", size=20, style="B")
        pdf.cell(w=250, h=40, txt=roommate1.name, border=0)
        pdf.cell(w=200, h=40, txt=roommate1_pay, border=0, ln=1)

        # Insertion of period and month
        pdf.cell(w=250, h=40, txt=roommate2.name, border=0)
        pdf.cell(w=200, h=40, txt=roommate2_pay, border=0, ln=1)

        pdf.output(self.file_name)
        webbrowser.open('file://' + os.path.realpath(self.file_name))


amount = float(input("Hi user, enter the bil amount!"))
period = input("What is the bill period?")
name1 = input("What is your name?")

print(f"Bill is {amount}")
days_in_house1 = int(input('How much did you stay in the apt.?'))

name2 = input("What is the other flatmate?")
days_in_house2 = int(input('How much did you stay in the apt.?'))


bill = Bill(amount=amount, period=period)
flatmate1 = Roommate(name=name1, days_in_house=days_in_house1)
flatmate2 = Roommate(name=name2, days_in_house=days_in_house2)

flatmate1.pays_bill(bill=bill, roommate2=flatmate2)
flatmate2.pays_bill(bill=bill, roommate2=flatmate1)
pdf_report = PDF_Reader(file_name='Report1.pdf')
pdf_report.generate(roommate1=flatmate1, roommate2=flatmate2, bill=bill)
