class cont_dest:
    x = 0

    def __init__(self,color,type):
        self.color = color
        self.type = type
        print("contsructor")

    def __del__(self):
        print("Destructor")

cd = cont_dest("black","SUV")
print(cd.color)
print(cd.type)