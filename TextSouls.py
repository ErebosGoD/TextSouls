import time
from typing import Text
import TextSoulsClasses
import TextSoulsEnemies
import TextSoulsWeapons
import TextSoulsItems

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
    print("So endet eure Reise nun.")
    time.sleep(1)
    print("Vielen Dank fürs Spielen!")

def character_creation():
    print("Very few found themselves at Firelink Shrine")
    time.sleep(2)
    print("Lost adventurer...")
    time.sleep(2)
    print("... recall your class")
    time.sleep(2)
    print("You can choose between...")
    time.sleep(2)
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
    print("Please choose between Wanderer, Knight, Thief, Bandit or Warrior")
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

def concerned_knight_dialog():
    print("Do you want to pay the merchant for his information? Yes/No")
    answer = input()
    if answer.lower() == "yes":
        print("You ask the merchant how much his information would cost")
        time.sleep(2)
        print("He tells you it would be around 20 gold")
        time.sleep(2)
        print("You hand over 20 gold and he points towards a upwards ridge along a cliffside")
        time.sleep(2)
        print("You need to go up and go straight 1 or 2 kilometers.")
        time.sleep(2)
        print("undead parish should be visible by then")
        adventurer.gold = adventurer.gold -20
        print("You shake his hand and went on your way towards the ridge")
    elif answer.lower() == "no":
        print("Fine then, try finding it on your own")
        time.sleep(2)
        print("But don't come back crying if you encounter any monsters")
        time.sleep(2)
        print("Without any sense of direction you head towards the ruins you can see north of yourself")
        time.sleep(2)
        #ruins()
    else :
        print("All of a sudden you see his eyes glowing bright red...")
        time.sleep(2)
        print("Before you can even begin to react he thrusts his sword into your chest...")
        time.sleep(2)
        game_over()



def firelink_shrine():
    time.sleep(2)
    print("You find yourself at Firelink Shrine in the lands of Lordran...")
    time.sleep(2)
    print("Your destiny is to ring the bell of awakening atop the church in undead parish...")
    time.sleep(2)
    print("before you sits a concerned looking knight...")
    time.sleep(2)
    print("He asked you what your name is")
    adventurer.name = input()
    print("Ahh, your name is "+ adventurer.name)
    time.sleep(2)
    print("You ask him about undead burg")
    time.sleep(2)
    print("Oh undead parish you say?...")
    time.sleep(2)
    print("undead parish is a cursed place")
    time.sleep(2)
    print("few dared to venture into that place...")
    time.sleep(2)
    print("... and even fewer returned alive.")
    time.sleep(2)
    print("You insist on going there")
    time.sleep(2)
    print("If you really want to know where to find undead parish, it will costs you some coin.")
    time.sleep(2)
    concerned_knight_dialog()

character_creation()