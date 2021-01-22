class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0 #to prevent encapsulation, double underscore turns attribute PRIVATE
        self.choice = ""
    
    def choose_symbol(self):
        self.choice = input(f"{self.name}, select rock(R), paper(P) or scissor(S): ")
        print(f"{self.name} selects {self.choice}")
    
    def numerical_choice(self):
        switcher = {
            "R": 0,
            "P": 1,
            "S": 2,
        }
        return switcher[self.choice]
    
    def add_point(self):
        self.points += 1
    
    def __str__(self):
        return self.name
              
class GameRound:
    def __init__(self,p1,p2):
        #rules matrix for symbol comparison(Rock, Paper, Scissor): 0(tie), 1(win), -1(loss)
        self.rules = [
            [0,-1,1],
            [1,0,-1],
            [-1,1,0]
        ]
        
        p1.choose_symbol()
        p2.choose_symbol()
        result = self.compare_choices(p1,p2)
        print(f"Round resulted in a {self.result_as_string(result)}")
        
        if result > 0:
            p1.add_point()
        elif result < 0:
            p2.add_point()
            
    def compare_choices(self, p1, p2):
        return self.rules[p1.numerical_choice()][p2.numerical_choice()]
    
    def result_as_string(self, result):
        res = {
            0: "Draw",
            1: "Win",
            -1: "Loss"
        }
        return res[result]
    
    def award_points():
        pass
            
class Game:
    def __init__(self):
        self.endGame = False
        self.firstplayer = Player(input("First Player Name: "))
        self.secondplayer = Player(input("Second Player Name: "))
    
    def start(self):
        while not self.endGame:
            GameRound(self.firstplayer, self.secondplayer)
            self.check_game_continue()
        
    def check_game_continue(self):
        answer = input("Continue game?(y/n)")
        if answer == "y":
            GameRound(self.firstplayer, self.secondplayer)
            self.check_game_continue()
        else:
            print(f"End of Game. {self.firstplayer} has {self.firstplayer.points}./n {self.secondplayer} has {self.secondplayer.points}")
            self.determine_winner()
            self.endGame = True
            
    def determine_winner(self):
        resultString = "It`s a Draw"
        if self.firstplayer.points > self.secondplayer.points:
            resultString = "{name} is the Winner".format(name=self.firstplayer)
        elif self.secondplayer.points > self.firstplayer.points:
            resultString = "{name} is the Winner".format(name=self.secondplayer)
        print(resultString)
        

game = Game()
game.start()
