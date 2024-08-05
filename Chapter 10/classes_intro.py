class Cat:
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color

    def meow(self):
        print("meow im " + self.name)
        self.name = "banana"
        print("nevermind now my name is " + self.name)

    def myName(self):
        print(self.name)