
class Framework:

    name:str

    language:str

    archi:str

    def set_framework(self,name,language,archi):

        self.name=name
        self.language=language
        self.archi=archi

    def display(self):

        print("name :",self.name)
        print("language :",self.language)
        print("architecture :",self.archi)
        print("===================")


django =Framework()

django.set_framework("mvt","python","ui")

django.display()

