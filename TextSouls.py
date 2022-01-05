import time
import random
from typing import Text
import TextSoulsClasses
import TextSoulsEnemies
import TextSoulsWeapons
import TextSoulsItems

timerBetweenLines2sec = time.sleep(2)

class adventurer:
    "blank stats for "
    name = ""
    level = 0
    strength = 0
    vitality = 0
    endurance = 0
    dexterity = 0
    gold = 0
    souls = 0

def game_over():
    print("And with that your journey ends")
    time.sleep(1)
    print("Thanks for playing")

def character_creation():
    print("Very few found themselves at Firelink Shrine")
    time.sleep(2)
    print("Lost adventurer...")
    time.sleep(2)
    print("... recall your class")
    time.sleep(2)
    print("You can choose between...")
    time.sleep(1)
    print("Wanderer,")
    time.sleep(1)
    print("Knight,")
    time.sleep(1)
    print("Thief,")
    time.sleep(1)
    print("Bandit")
    time.sleep(1)
    print("or Warrior")
    time.sleep(1)
    print("Please type one of the above")
    class_picked = input()
    if class_picked.lower() == "wanderer":
        adventurer.level = TextSoulsClasses.wanderer.level
        adventurer.strength = TextSoulsClasses.wanderer.strength
        adventurer.vitality = TextSoulsClasses.wanderer.vitality
        adventurer.endurance = TextSoulsClasses.wanderer.endurance
        adventurer.dexterity = TextSoulsClasses.wanderer.dexterity
        adventurer.gold = TextSoulsClasses.wanderer.gold
        adventurer.souls = TextSoulsClasses.wanderer.souls
        firelink_shrine()
    elif class_picked.lower() == "knight":
        adventurer.level = TextSoulsClasses.knight.level
        adventurer.strength = TextSoulsClasses.knight.strength
        adventurer.vitality = TextSoulsClasses.knight.vitality
        adventurer.endurance = TextSoulsClasses.knight.endurance
        adventurer.dexterity = TextSoulsClasses.knight.dexterity
        adventurer.gold = TextSoulsClasses.knight.gold
        adventurer.souls = TextSoulsClasses.knight.souls
        firelink_shrine()
    elif class_picked.lower() == "thief":
        adventurer.level = TextSoulsClasses.thief.level
        adventurer.strength = TextSoulsClasses.thief.strength
        adventurer.vitality = TextSoulsClasses.thief.vitality
        adventurer.endurance = TextSoulsClasses.thief.endurance
        adventurer.dexterity = TextSoulsClasses.thief.dexterity
        adventurer.gold = TextSoulsClasses.thief.gold
        adventurer.souls = TextSoulsClasses.thief.souls
        firelink_shrine()
    elif class_picked.lower() == "bandit":
        adventurer.level = TextSoulsClasses.bandit.level
        adventurer.strength = TextSoulsClasses.bandit.strength
        adventurer.vitality = TextSoulsClasses.bandit.vitality
        adventurer.endurance = TextSoulsClasses.bandit.endurance
        adventurer.dexterity = TextSoulsClasses.bandit.dexterity
        adventurer.gold = TextSoulsClasses.bandit.gold
        adventurer.souls = TextSoulsClasses.bandit.souls
        firelink_shrine()
    elif class_picked.lower() == "warrior":
        adventurer.level = TextSoulsClasses.warrior.level
        adventurer.strength = TextSoulsClasses.warrior.strength
        adventurer.vitality = TextSoulsClasses.warrior.vitality
        adventurer.endurance = TextSoulsClasses.warrior.endurance
        adventurer.dexterity = TextSoulsClasses.warrior.dexterity
        adventurer.gold = TextSoulsClasses.warrior.gold
        adventurer.souls = TextSoulsClasses.warrior.souls
        firelink_shrine()
    else :
        game_over()

def firelink_shrine():
    time.sleep(2)
    print("You arrive at Firelink Shrine in the lands of Lordran...")
    time.sleep(2)
    print("Your destiny is to ring the bell of awakening atop the church in undead parish...")
    time.sleep(3)
    print("before you sits a concerned looking knight...")
    time.sleep(2)
    print("He asked you what your name is")
    adventurer.name = input()
    print("Ahh, your name is "+ adventurer.name)
    time.sleep(2)
    print("You ask him about undead parish")
    time.sleep(2)
    print("Oh undead parish you say?...")
    time.sleep(2)
    print("undead parish is a cursed place")
    time.sleep(2)
    print("few dared to venture into that place...")
    time.sleep(2)
    print("... and even fewer returned alive.")
    time.sleep(2)
    print("\"You insist on going there\"")
    time.sleep(2)
    print("If you really want to know where to find undead parish, it will costs you some coin.")
    time.sleep(2)
    concerned_knight_dialog()

def concerned_knight_dialog():
    print("Do you want to pay the merchant for his information? Yes/No")
    answer = input()
    if answer.lower() == "yes":
        print("You ask the knight how much his information would cost")
        time.sleep(2)
        print("He tells you it would be around 20 gold")
        time.sleep(2)
        print("You hand over 20 gold and he points towards a upwards ridge along a cliffside")
        time.sleep(2)
        print("You need to go up and go straight 1 or 2 kilometers.")
        time.sleep(2)
        print("undead parish should be visible by then")
        adventurer.gold = adventurer.gold -20
        time.sleep(2)
        print("You shake his hand and went on your way towards the ridge")
        time.sleep(2)
        ridgeAfterFirelink()
    elif answer.lower() == "no":
        print("Fine then, try finding it on your own")
        time.sleep(2)
        print("But don't come back crying if you encounter any monsters")
        time.sleep(2)
        print("Without any sense of direction you head towards the ruins you can see north of yourself")
        time.sleep(2)
        ruins()
    else :
        print("All of a sudden you see his eyes glowing bright red...")
        time.sleep(2)
        print("Before you can even begin to react he thrusts his sword into your chest...")
        time.sleep(2)
        game_over()

def  ridgeAfterFirelink():
    time.sleep(2)
    print("You arrive at the ridge")
    time.sleep(2)
    print("Some parts look very narrow...")
    time.sleep(2)
    print("...almost too narrow to walk on")
    time.sleep(2)
    print("You can make out some sort of small plateau after the narrow parts")
    time.sleep(2)
    print("Do you want to tread carefully (tread) or rush towards it (rush)")
    answer = input()
    if answer.lower == "tread":
        time.sleep(2)
        print("You decide to tread carefully")
        time.sleep(2)
        print("As you go up the slope the path grows narrower by the step")
        time.sleep(2)
        print("But since you decided to take your time your steps are steadfast")
        time.sleep(2)
        print("After some time you arrive at the plateau")
        time.sleep(2)
        print("Atop you see another staircase guarded by an undead soldier")
        time.sleep(2)
        print("Seems like you have no choice but to fight")
        time.sleep(2)
        #hollow_soldier_fight1()
    elif answer.lower == "rush":
        rush_chance = random.randint(1,20) + adventurer.dexterity
        time.sleep(2)
        print("Being confident in your athletic abilities,")
        time.sleep(1)
        print("you decided to rush upwards")
        time.sleep(2)
        if rush_chance >= 25:
            print("Light as feather, you jump from step to step")
            time.sleep(2)
            print("In a heartbeat you reach the top and see another staircase guarded by an undead soldier")
            time.sleep(2)
            print("Seems like you have no choice but to fight")
            time.sleep(2)
            #hollow_soldier_fight1()
        elif rush_chance in range (10,24):
            grab_chance = random.randint(1,20) + adventurer.dexterity
            print("Suddenly you foot slips right as you take the next step")
            time.sleep(2)
            print("Without much time to think your only option is trying to grab the ledge (grab)...")
            time.sleep(2)
            if grab_chance >= 25:
                print("At the last second you can grab hold of the ledge")
                time.sleep(1)
                print("As you climb towards the plateau you heart rate slowly goes down")
                time.sleep(1)
                print("having escaped a near-death scenario just now.")
                time.sleep(2)
                print("Atop you see another staircase guarded by an undead soldier")
                time.sleep(2)
                print("Seems like you have no choice but to fight")
                time.sleep(2)
                #hollow_soldier_fight1()
            elif grab_chance < 25:
                print("You extend your arm towards the ledge...")
                time.sleep(2)
                print("...trying to grab a hold of it")
                time.sleep(2)
                print("but sadly your reach is not enough")
                time.sleep(2)
                print("as you fall your life flashes before your eyes")    
                time.sleep(2)
                print("With a loud splash your body hits the bottom")
                time.sleep(2)
                game_over()
            else:
                print("You sadly took too much time to think and are now falling towards you death")
                time.sleep(2)
                game_over()
        else:
            print("Your mind wandered off as you moved towards it")
            time.sleep(2)
            print("As you slowly realize...")
            time.sleep(2)
            print("You overstepped the ledge and are now falling towards your death")
            time.sleep(2)
            game_over()       
    else:
            print("Your mind wandered off as you moved towards it")
            time.sleep(2)
            print("As you slowly realize...")
            time.sleep(2)
            print("You overstepped the ledge and are now falling towards your death")
            time.sleep(2)
            game_over()       

            


def ruins():
    time.sleep(2)
    print("After a few minutes you reached the ruins")
    time.sleep(2)
    print("Time really took its toll on the building that once stood here")
    time.sleep(2)
    print("The walls have huge parts missing...")
    time.sleep(2)
    print("...and moss grows over almost every brick") 
    time.sleep(2)
    print("As you navigate through the rubble...")
    time.sleep(2)
    print("...the path splits to either left or right")
    time.sleep(2)
    print("Which way to you want to go?")
    answer = input()
    if answer.lower() == "left":
        ruins_left()
        

def ruins_left():
    time.sleep(2)
    print("You decide to go to the left")
    time.sleep(2)
    print("You arrive at a surprisingly intact house")
    time.sleep(2)
    print("It seems to have belonged to a noble or something similar...")
    time.sleep(2)
    print("But looking closer you can still see the cracks in the wall")
    time.sleep(2)
    print("You decide to enter regardless")
    time.sleep(2)
    print("The entrance hall is empty,...")
    time.sleep(2)
    print("...likely because some bandits were here")
    time.sleep(2)
    print("looking around you spy a trapdoor")
    time.sleep(2)
    print("After opening the heavy iron door you see a dimly lit room with a bulky figure standing in the corner")
    time.sleep(2)
    print("Approaching the figure you ask yourself...")
    time.sleep(2)
    print("..who could that be?")
    time.sleep(2)
    print("That question would soon be answered...")
    time.sleep(2)
    print("...as the figure turns around and looks directly at you!")
    time.sleep(2)
    print("It is wearing heavy stone armor with what seems to be a dragons tooth as a weapon")
    time.sleep(2)
    print("before you can climb back up the figure lunges at you...")
    time.sleep(2)
    print("...leaving you no choice but to fight for you life")
    havel_fight()

def havel_fight():
    time.sleep(2)
    print("The figure starts swinging its gigantic, dragon tooth-like club your way")
    time.sleep(2)
    print("Would you try to block it (block)...")
    time.sleep(2)
    print("...or try to dodge to the side (dodge)?")
    answer = input()
    if answer.lower() == "block":
        time.sleep(2)
        print("You decide to try to block the incoming attack")
        time.sleep(2)
        chance_block = random.randint(1,20) + adventurer.strength
        if chance_block >= 30:
            time.sleep(2)
            print("You hold you equipped shield before your body, hoping it would soften the incoming blow...")
            time.sleep(2)
            print("Regardless of you blocking attempt the blow sends you crashing into the wall behind you")
            time.sleep(2)
            print("Your head spins from the impact")
            time.sleep(2)
            print("You wobble back on your feet")
            time.sleep(2)
            print("Seeing the figure walking towards you")
            time.sleep(2)
            havel_fight()
        else:
            time.sleep(2)
            print("Frozen in fear you drop your shield...")
            time.sleep(2)
            print("As you see the club coming towards your head your life flashes before your eyes")
            time.sleep(2)
            print("seconds seem like hours...")
            time.sleep(2)
            print("...and you can't do anything to stop the blow")
            time.sleep(2)
            print("With a loud crack the dragons tooth crushes your skull")
            time.sleep(2)
            print("Better to leave one of Havel's Knights alone")
            time.sleep(2)
            game_over()
    elif answer.lower() == "dodge":
        time.sleep(2)
        print("You decide to try and dodge the incoming attack")
        time.sleep(2)
        chance_dodge = random.randint(1,20) + adventurer.dexterity
        if chance_dodge >= 30:
            time.sleep(2)
            print("Your body feels light as feather")
            time.sleep(2)
            print("But still, you barely manage to dodge the blow from the figure")
            time.sleep(2)
            print("The enemy doesn't give you much time to think")
            time.sleep(2)
            print("It lets out an angry cry coming at you again")
            havel_fight()
        else:
            time.sleep(2)
            print("Frozen in fear, your body won't move")
            time.sleep(2)
            print("while the club comes roaring towards you, you can just stand there and watch")
            time.sleep(2)
            print("seconds seem like hours...")
            time.sleep(2)
            print("...and you can't do anything to dodge the blow")
            time.sleep(2)
            print("With a loud crack the dragons tooth crushes your skull")
            time.sleep(2)
            print("Better to leave one of Havel's Knights alone")
            time.sleep(2)
            game_over()   
    else:
        time.sleep(2)
        print("Without leaving you much time to think")
        time.sleep(2)
        print("the figure sends its weapon crashing down on you skull")
        time.sleep(2)
        game_over()        



character_creation()