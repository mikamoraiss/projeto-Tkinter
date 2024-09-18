from controller import Controller

class Main():
    def __init__(self):
        self.controller = Controller()
    
    def executar(self):
        self.controller.visualizar()
    
main = Main()
main.executar()

