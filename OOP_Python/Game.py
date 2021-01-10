class Participant():
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_symbol(self, symbol):
        self.symbol = symbol


class Game():
    def __init__(self):        
        self.name = input(print("What's your name?: "))
        self.participantOne = Participant(self.name)
    
        self.name = input(print("What's your name?: "))
        self.participantTwo = Participant(self.name)
    
    def choose_symbol(self):        
        self.participantOne.set_symbol(input(print(f"{self.participantOne.get_name()} What's symbol ")))
        self.participantTwo.set_symbol(input(print(f"{self.participantTwo.get_name()} What's symbol ")))

if __name__ == '__main__':
    game = Game()
    game.choose_symbol()

