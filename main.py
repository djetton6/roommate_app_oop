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
        self.file_name

    def generate(self, roommate1, roommate2, bill):
        pass


bill = Bill(amount=120, period='March 2021')
desmend = Roommate(name="Desmend", days_in_house=20)
mary = Roommate(name="Dan", days_in_house=25)

print('Desmend pays:', desmend.pays_bill(bill=bill, roommate2=mary))
print('Mary pays:', mary.pays_bill(bill=bill, roommate2=desmend))
