# we define the student class and the hello method
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

# we defing an action method of the raising hand metod
    def raise_hand(self):
        print("Pick me!")

# defining the objects class that will inherit from the student class, and define a mehod of hello then call the hello from the parent class which prints the greeting
class ChattyStudent(Student): 
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
# using super to call the rasing hand method from the parent class
    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()