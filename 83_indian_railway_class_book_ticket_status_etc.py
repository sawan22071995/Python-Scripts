class Train:
    company = 'Indian Railway'
    def __init__(self,trainno):
        self.trainno = trainno
    def getStaus(self,seats):
        self.seats = seats
    def getFare(self):
        fare = self.seats * 1800
        return fare
    def bookTicket(self):
        return f"your {self.seats} in tarin {self.trainno} seat is booked succesfully!!"
    def getTicket(self):
        print(f"****************************{Train.company}**********************")
        print(f"Train no : {self.trainno}")
        print(f"Total no of tickets : {self.seats}")
        print("Congratulation")
        print(f"You booked ticket successfully")

visitor = Train(11200)
visitor.getStaus(3)
visitor.bookTicket()
visitor.getTicket()
print(f"The fare is : {visitor.getFare()}")