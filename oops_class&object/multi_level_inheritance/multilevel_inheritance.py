
class GrandParent:

    def properties(self):

        print("12 cent land with house")

class Parent(GrandParent):

    def vehicle(self):

        print("swift car")

class Child(Parent):

    def gadgets(self):

        print("iphone,laptop")


child_instance =Child()

child_instance.properties()

child_instance.vehicle()

child_instance.gadgets()