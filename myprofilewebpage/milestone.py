class Tech:
    name = "Tech camp"


class Payroll(Tech):
    basic = 0
    benefits = 0
    gross = 0
    paye = 0

    def __init__(self, a, b):
        self.basic = a
        self.benefits = b
        self.grossSalary()
        self.paye

    def grossSalary(self):
        self.gross = self.basic + self.benefits
    def payE(self,ax):
        if self.gross <= 12298:
            self.paye = 12298 * 0.1
            ax = self.gross - 12298
        elif ax in range(12299, 23885):
            self.paye = 11587 * 0.15
        elif self.gross in range(23886, 35472):
            self.paye = 11587 * 0.2
        elif self.gross in range(35473, 47059):
            self.paye = 11587 * 0.25
        elif self.gross in range(35473, 47059):
        self.paye = 11587 * 0.25
    def N_HIF(self):
        if self.gross <= 5999:
            print(self.gross - 150)






