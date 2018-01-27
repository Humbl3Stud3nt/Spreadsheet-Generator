class Member:
    def __init__(self, **kwargs):
        self.attributes = ("FIRST NAME", "LAST NAME", "FORM", "DUES PAID")
        self.duesPaid = 0.0

        if "club" in kwargs.keys():
            self.club = kwargs["club"]
        else:
            self.club = str(None)

        if "name" in kwargs.keys():
            self.name = kwargs["name"].split(" ")
        else:
            self.name = "BOB DYLAN".split(" ")

        self.firstName = self.name[0].capitalize()
        self.lastName = self.name[1].capitalize()

        if "duesPaid" in kwargs.keys():
            self.duesPaid += float(kwargs["duesPaid"])

        if "form" in kwargs.keys():
            self.form = kwargs["form"]
        else:
            self.form = "0-0"

    def setName(self, name):
        firstName, lastName = name.split(" ")
        self.firstName, self.lastName = firstName, lastName

    def getName(self):
        return self.firstName, self.lastName

    def setClub(self, club):
        self.club = club

    def getClub(self):
        return self.club

    def setDues(self, dues):
        self.duesPaid = dues

    def getDues(self):
        return self.duesPaid

    def setForm(self, form):
        self.form = form

    def getForm(self):
        return self.form

    def update(self, **kwargs):
        self.club = kwargs["club"]
        self.name = kwargs["name"].split(" ")
        self.firstName = kwargs["firstName"]
        self.lastName = kwargs["firstName"]
        self.duesPaid += float(kwargs["duesPaid"])
        self.form = kwargs["form"]
