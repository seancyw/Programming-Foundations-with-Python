class Parent() :
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def showInfo(self) :
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)

#class child inherit all the attribute from parent
class Child(Parent) :
    def __init__(self, last_name, eye_color, toys_number) :
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.toys_number = toys_number

    #Overriding function on Parent class
    def showInfo(self) :
        #Parent.showInfo(self)
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)
        print("Toy number: ", self.toys_number)

billy_cyrus = Parent("Cyrus", "Blue")
print(billy_cyrus.last_name)
billy_cyrus.showInfo()

miley_cyrus = Child("Cyrus", "Red", 10)
print(miley_cyrus.last_name)
print(miley_cyrus.toys_number)
miley_cyrus.showInfo()
