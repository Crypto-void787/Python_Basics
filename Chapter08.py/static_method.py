''' Static Method : Method that dont use the self parameters (work at class level) '''


class Greet :
    @staticmethod   #decorator 
    def greeting() :
        print("Hello")



g = Greet()
g.greeting()        