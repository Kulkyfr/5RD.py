# Date: 11/7/24
# author: <ekulkin2809002@woonsocketschools.com>
# author:
# author:
# project: 5RD

import random, time

#from gzip import write32u

#time.sleep(2)
#os.system(clear)
bridgeChoice=True
dabloons = 0
playerStrength = 0
playerDexterity = 0
playerConstitution = 0
playerIntelligence = 0
playerWisdom = 0
playerCharisma = 0
playerHealth = 0
playerSpeed = 0
playerInititive = 0
playerAttack = 0
playerName = input("Salutations! What's your name?: ")
print("Great to meet you", playerName, "Im Dan the demigod. I am the Ancestry and Class distributer. Here are the classes")
time.sleep(4.75)
playerClass = input("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Classes are: Alchemist, Adventurer, Fighter, and a Sorcerer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Alchemists- are very skilled in potions.             2) Adventurers- are very outdoorsy with a "Spare Axe"
They can make a plethora of potions.                    and a "Torch" in which they can light out of thin air.
They carry a "Potion Maker" and "Crafting Box".         They allow +1 intelligence.
With +1 dexterity.

3) Fighters- are pure attacking phenoms.                4) Sorcerers- use many different spells to conjure up
They use "Brass Knuckles" along with                    all types of attacks. They use a "Magic Wand" to
"Noradrenaline Drink" to help fuel their punches.       help focus a set amount of power into one place
+1 strength                                             (the wand.) +1 wisdom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now what Class would you like? Please pick a number 1-4: """)
classes=True
while classes:
    if playerClass == "1":
        print("Alchemist it is!")
        playerDexterity+=1
        break
    elif playerClass == "2":
        print("So an adventurer? Amazing.")
        playerIntelligence+=1
        break
    elif playerClass == "3":
        print("A Fighting class? Great choice.")
        playerStrength+=1
        break
    elif playerClass == "4":
        print("Sorcerer. Ahh, very popular and smart choice.")
        playerWisdom+=1
        break
    else:
        print("Pick a number1-4, please restart.")
        continue
time.sleep(2)
playerAncestry = input("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Ancestries include: Elves, Goblins, Dwarves, Halflings, and Humans.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Humans- are simply the baseline of all races.        4) Goblins- are very similar to the Dwarves. 
intelligent creatures. With +2 intelligence,            They are the smelly slimey version of chihuahuas.

2) Dwarves- are small humans                            5) Wizards- are entirely long range fighters.  
with better battle IQ. +2 dexterity                     +2 wisdom                 

3) Elves- are very smart and
+1 all attributes.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now what Ancestry would you like? Please pick a number from 1-5: """)
if playerAncestry == "1":
    print("Human it is!")
    playerIntelligence+=2
elif playerAncestry == "2":
    print("So a Goblin?")
    playerConstitution+=1
    playerStrength+=1
elif playerAncestry == "3":
    print("A Halfling ancestry? Okay.")
    playerDexterity+=2
elif playerAncestry == "4":
    print("That will be a Wizard.")
    playerWisdom+=2
elif playerAncestry == "5":
    print("So a Elf? smart choice!")
else:
    print("Thats not a real ancestry. Please restart.")
print("Amazing. Lets set up your attributes.")
if playerAncestry == "1":
    print('''
        As a human, you get two free Boosts
        You can boost your [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma
    ''')
    playerSpeed = 25
    playerHealth = 8
    isChoosing = True
    while isChoosing is True:
        playerBoost1 = input("Your first boost is to : ")
        playerBoost2 = input("Your second boost is to : ")
        if playerBoost1 == playerBoost2:
            print("You can't boost the same ability twice")
        else:
            if playerBoost1 == "S" or playerBoost2 == "S":
                playerStrength += 1
            elif playerBoost1 == "D" or playerBoost2 == "D":
                playerDexterity += 1
            elif playerBoost1 == "C" or playerBoost2 == "C":
                playerConstitution += 1
            elif playerBoost1 == "I" or playerBoost2 == "I":
                playerIntelligence += 1
            elif playerBoost1 == "W" or playerBoost2 == "W":
                playerWisdom += 1
            elif playerBoost1 == "Ch" or playerBoost2 == "Ch":
                playerCharisma += 1
            isChoosing = False

elif playerAncestry == "2":
    print('''
        As a dwarf, you take a penalty to Charisma.
        You can boost your Constitution or your Strength and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 20 feet per round and you start with 10 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [C]onstitution or your [S]trength? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerCharisma += -1
    if playerBoost1 == "S" or playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost1 == "C" or playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

elif playerAncestry == "3":
    print('''
        As an elf, you take a penalty to Strength.
        You can boost your Dexterity or your Intelligence and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 30 feet per round and you start with 6 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10
elif playerAncestry == "4":
    print('''
            As an Goblin, you take a penalty to intelligence.
            You can boost your Dexterity or your Constitution and you get one free boost.
            [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

            Your Speed is 30 feet per round and you start with 6 Health.
        ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerIntelligence += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 10
    playerHealth = 20
elif playerAncestry == "5":
    print('''
        As an Wizard, you take a penalty to Strength.
        You can boost your Dexterity or your Intelligence and you get one free boost.
        [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

        Your Speed is 30 feet per round and you start with 6 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 10
    playerHealth = 20
dabloonLoop = True
while dabloonLoop:
    dabloon = input("As you walk you notice a subtle rustling in the bushes to your left. What will you do? [C]heck? Or [I]gnore: ")
    if dabloon == "C":
        print("Check. Great choice. In fact the best choice! You find a dabloon! You may need this soon.")
        dabloons+=1
        break
    elif dabloon == "I":
        print("Ignore? Okay, if you insist.")
        break
    else:
        print("Please type 'C' or 'I'.")
time.sleep(2.5)
bridge = True
print("You are walking,")
time.sleep(2)
print("and walking,")
time.sleep(2)
print("and walking,")
time.sleep(2.5)
while bridge:
    bridge1choice=input("""Then you find a bridge. And all of a suddon, out pops a Troll!     
He says, "You! Traveler! Give me a dabloon now!" Will you [U]se your dabloon you found in those bushes, or do [N]othing becuase you NEVER SEARCHED THOSE BUSHES THAT WOULD HAVE HELPED YOU! So what will it be?: """)
    if bridge1choice == "U":
        if dabloons<1:
            print("""You dont have a dabloon! What were you thinking! "You said you have a dabloon for troll? Where us that dabloon? Well it looks like you dont have one!" You die.""")
        elif dabloons>=1:
            print(""""Well well well. I guess you got lucky. Next time I will need more! nowing you have a dabloon! Til we meet again traveler!" You live. For now...""")
        break
    elif bridge1choice == "N":
        print("""Uh oh... wrong choice... "No dabloon for Troll? No breathing for you! Perish!!" You have been vanquished. You will live in purgatory!!!
(Just an infinite loop.)""")
        bridge == False
    else:
        print("Please type 'U' or 'N'.")
time.sleep(2)
gate=True
ogre=True
ogreHealth = 15
while gate == True:
    print("After that annoying Troll interaction, you find yourself at the front of a MASSIVE gate. You see a large ogre and decide to walk over to it")
    print("""He talks to you. "Who goes there! What is your business in these parts?""")
    time.sleep(2)
    print("Just wandering you say?")
    gate2Choice=input("""Not a valid reason. I shall Duel you to see if you are worthy enough to enter Troll Ville!"
Do you [F]ight? and prove you are worthy? Or [R]un away into the sunset.""")
    if gate2Choice == "F":
        print("You shall fight to prove your worth!")
        while ogre:
            print("""As to deliveer your first blow, the ogre has 15 health. You have 100, so the foe is quite weak. How ever, you may never regenerate. Unless... (alchemist potions)""")
            ogreBlow1=(playerStrength+playerDexterity+(random.randint(1,10)))
            if ogreBlow1<ogreHealth:
                print("""Close but you haven't vanquished the foe quite yet. He attacks."That had no power behind it. It's starting to look like you arent strong enouggghhh!""")
                ogre == True
            elif ogreBlow1>ogreHealth:
                print(""" "Well im not sure how you beat me first try but you are MORE than worthy to pass," You enter Troll Ville. Have fun!""")
                break
            ogreBlow2=(playerStrength+playerDexterity+(random.randint(1,10)))
            if ogreBlow2<ogreHealth:
                print(""" "You've hurt me bad, yet not enough! Keep it coming!" You haven't defeated him yet. Keep trying!""")
                ogre == True
            elif ogreBlow2>ogreHealth:
                print(""" "2 Tries? I lay defeated after two measily attempts? You must be a truly gifted adversary. You pass."
He lets you into Troll Ville.""")
                break
            ogreBlow3=(playerStrength+playerDexterity+(random.randint(1,10)))
            if ogreBlow3<ogreHealth:
                print(""" "Still havent beaten me? Just as something i'd expect from a low class warrior. Keep on trying!"
Hes still standing.""")
                ogre == True
            elif ogreBlow3>ogreHealth:
                print(""" "Ahh finally. I'd say your worthy. Come on through." You pass. Just barely...""")
                break
            ogreBlow4=(playerStrength+playerDexterity+(random.randint(1,10)))
            if ogreBlow4<ogreHealth:
                print(""" "Youve yet to vanquish me? How weak you are."
He still stands. Attack once more or be banished from Troll Ville. """)
                ogre == True
            elif ogreBlow4>ogreHealth:
                print(""" "4 tries. It took you 4 tries. Ill let you in, but man your weak."
You pass on the verge of a hair. """)
                break
            ogreBlow5=(playerStrength+playerDexterity+(random.randint(1,10)))
            if ogreBlow5<ogreHealth:
                print(""" "You. You! YOU! YOU HAVE THE AUDACITY TO ATTEMPT TROLL VILLE PASSAGE WHEN YOU CANT DEFEAT ME THROUGH THE SPAN ON 5 ATTACKS???
5 ATTACKS!!! BEGONE! YOU ARE HEREFORTH BANISHED FROM TROLL VILLE!!!" You get banished and frolick into the sunset. Never to be seen again.""")
                ogre==False
            elif ogreBlow5>ogreHealth:
                print(""" "Finally! 5 attemps later! You have won. You pass for now. Tread lightly weary foe."
You pass from the length of a flea.""")
                break
    elif gate2Choice == "R":
        print("You run far far away... never to be seen again. Your story ends here.")
    else:
        print("Please pick [F] or [R].")
        gate2Choice==True
