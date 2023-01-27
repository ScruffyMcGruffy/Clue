import random 


class Player():

    def __init__(self):

        #value = input("type here")
        self.playerList = []
        self.numPlayers = int(input("Number of players_"))
        
            
        for x in range(self.numPlayers):
            self.playerList.append(input("Say your name_"))

class GamePlay():

    #def intro(self):
       

    def __init__(self): 
        self.copysuspects = ['MistaWhite', 'Mr.Greeb', 'Porpol', 'Ms.Yellowb', 'INDIGO', 'Mrs.Bule', 'The Red One', 'Mr.Pink']
        self.copyweapons = ['gun', 'baseball bat', 'katana', ' frying pan', 'giant cartoon hammer', 'bowling ball', '100 men', 'illicit substances']
        self.copyrooms = ['entrance', 'kitchen', 'pool', 'living room', 'hallway', 'arboretum', 'bedroom', 'bathroom']

        self.suspects = {1: 'MistaWhite', 2: 'Mr.Greeb', 3: 'Porpol', 4: 'Ms.Yellowb', 5: 'INDIGO', 6: 'Mrs.Bule', 7: 'The Red One', 8: 'Mr.Pink'}
        self.weapons = {1: 'gun', 2: 'baseball bat', 3: 'katana', 4: ' frying pan', 5: 'giant cartoon hammer', 6: 'bowling ball', 7: '100 men', 8: 'illicit substances'}
        self.rooms = {1: 'entrance', 2: 'kitchen', 3: 'pool', 4: 'living room', 5: 'hallway', 6: 'arboretum', 7: 'bedroom', 8: 'bathroom'}
        
        x = Player()
        self.playerList = x.playerList
        self.killingblow = {'murder weapon': random.choice(list(self.weapons.values()))}
        self.theroom = {'death room': random.choice(list(self.rooms.values()))}
        self.crimes = {'guilty': self.suspects.pop(random.randrange(0, len(self.suspects)))}
        #self.dead = {'murdered': self.suspects.pop(random.randrange(0, len(self.suspects)))}
        #self.suspects.pop(random.randrange(0, len(self.suspects)))
        self.current_player = 0
        counter = 0
        Interrogate = 0
        def setinterrogate():
            Interrogate = random.choice(self.suspects)

        #self.intro()

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Amongus Manor, there has been a terrible murder tonight. Can you help us solve the case?")
        print("Explore a new room: R   Inspect a room: I   Interrogate a suspect: S   Make a case: M")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.crimes)
        print(self.killingblow)
        print(self.theroom)
        #print("Oh no! " + str(self.dead) + "has been murdered! How did they die?")

        

            

        while self.playerList.__len__() > 0:
            currentPlay = self.playerList.pop(0)

            value = input("What do you want to do, " + str(currentPlay) + "?")

            if value == 's':
                
                setinterrogate() 

                if Interrogate == self.crimes:
                    print("You interogated: " + str(Interrogate) + " and they acted suspicious...")
                else:
                    print("You interrogated: " + str(Interrogate) + " and cleared their name!")

            if value == 'r':
                print("You walked into: " + random.choice(self.rooms) + " and did not discover a body.")

            self.playerList.append(currentPlay)

            if value == 'm':
                option1 = input("Who is the killer? " + "The options are " + str(self.suspects) + ".")
                if option1 == self.guilty["Suspect"]:
                    counter = counter + 1

                option2 = input("What was the weapon? " + "The options are " + str(self.weapons) + ".")
                if option2 == self.whodidit["Weapon"]:
                    counter = counter + 1

                option3 = input("What room was the murder in? " + "The options are " + str(self.rooms) + ".")
                if option3 == self.whodidit["Room"]:
                    counter = counter + 1

                if counter < 3:
                    print('wrong, you died becasue you guessed wrong. No evidence? (TnT)')
                    self.playerList.pop(self.playerList.__len__() - 1)

                if counter == 3:
                    print('The murderer has been put to rest, congratultions!')
                    self.playerList.clear()






if __name__ == "__main__":
    GamePlay()