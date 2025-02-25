class Father:
    def show(self):
        print("parent1")
class Mother:
    def show(self):
        print("parent2")
class child(Father,Mother):
    super().show()
    
obj=child()
obj.show()
