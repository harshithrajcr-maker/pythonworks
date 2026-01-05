
from abc import ABC

from abc import abstractmethod

class Editor:
    
    @abstractmethod
    def create_module_and_package(self):

        pass

    @abstractmethod
    def edit(self):

        pass
    
    @abstractmethod
    def execute(self):

        pass
    
    @abstractmethod
    def debug(self):

        pass


class VsCode(Editor):

    def create_module_and_package(self):
        
        print("vs code create modules and package")

    def edit(self):
        
        print("vscode edit")

    def execute(self):
        
        print("vscode execute")

    def debug(self):
        
        print("vscode debuging")

vscode_instance =VsCode()

vscode_instance.create_module_and_package()
vscode_instance.debug()
vscode_instance.edit()
vscode_instance.execute()