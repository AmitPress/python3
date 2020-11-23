# class Human:
#     def __init__(self):
#         pass


# class Footballer:
#     def __init__(self, agility, goals, position):
#         self.agility = agility
#         self.goals = goals
#         self.position = position


# class Batsman:
#     def __init__(self, runs, high_score):
#         self.runs = runs
#         self.high_score = high_score


# class Bowler:
#     def __init__(self, wickets, best_score):
#         self.wickets = wickets
#         self.best_score = best_score


# class Cricketer(Batsman, Bowler, Human):
#     def __init__(self, designation, runs=None, high_score=None, wickets=None, best_score=None): # default parameters
#         if designation == "batsman":
#             Batsman.__init__(self, runs, high_score)
#         if designation == "bowler":
#             Bowler.__init__(self, wickets, best_score)
    
# sreyas = Cricketer("batsman", 2347, 122) # orderly put arguments

# print(sreyas.high_score) # -> 122

# rohit = Cricketer("bowler", wickets = 121, best_score = {"3":30}) # arbitrary parameters

# print(rohit.best_score) # -> ('3':30)

# # lets have a look upon whats inside best_score

# print(rohit.best_score["3"]) # -> 30


# this is not a good practice I think. Because I this manner we did a bottom up. How? We first wrote Batsman & Bowler then did write a Cricketer class. It violets a principle that tells "we are human first".
# so if a person is a person he is also a human, thats simply indicates if you are a person then you must be a human. So, human is the major charecteristic. So, Person should depend on Human. Hence, the dependency list is valid a normal as it follows the rule of the nature
# again oop is too much relatable with our real world senerios


# now we will dicuss the legitimate and best way to do inheritance





# the rules of delegating parameters of special type is really one directional, I said it in this sense that we are using same syntax to do different things
# on the core file we will discuss more about it