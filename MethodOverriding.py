class Parent:
    def show(self):
        print("parent class")
class Child(Parent):
    def show(self):
        super().show()
        print("child class")
class GChild(Child):
    def show(self):
        super().show()
        print("GChild class")
obj=GChild()
obj.show()
