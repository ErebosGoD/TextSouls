import time
import random
import area_FirelinkShrine
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
        area_FirelinkShrine.firelink_shrine()
    elif class_picked.lower() == "knight":
        adventurer.level = TextSoulsClasses.knight.level
        adventurer.strength = TextSoulsClasses.knight.strength
        adventurer.vitality = TextSoulsClasses.knight.vitality
        adventurer.endurance = TextSoulsClasses.knight.endurance
        adventurer.dexterity = TextSoulsClasses.knight.dexterity
        adventurer.gold = TextSoulsClasses.knight.gold
        adventurer.souls = TextSoulsClasses.knight.souls
        area_FirelinkShrine.firelink_shrine()
    elif class_picked.lower() == "thief":
        adventurer.level = TextSoulsClasses.thief.level
        adventurer.strength = TextSoulsClasses.thief.strength
        adventurer.vitality = TextSoulsClasses.thief.vitality
        adventurer.endurance = TextSoulsClasses.thief.endurance
        adventurer.dexterity = TextSoulsClasses.thief.dexterity
        adventurer.gold = TextSoulsClasses.thief.gold
        adventurer.souls = TextSoulsClasses.thief.souls
        area_FirelinkShrine.firelink_shrine()
    elif class_picked.lower() == "bandit":
        adventurer.level = TextSoulsClasses.bandit.level
        adventurer.strength = TextSoulsClasses.bandit.strength
        adventurer.vitality = TextSoulsClasses.bandit.vitality
        adventurer.endurance = TextSoulsClasses.bandit.endurance
        adventurer.dexterity = TextSoulsClasses.bandit.dexterity
        adventurer.gold = TextSoulsClasses.bandit.gold
        adventurer.souls = TextSoulsClasses.bandit.souls
        area_FirelinkShrine.firelink_shrine()
    elif class_picked.lower() == "warrior":
        adventurer.level = TextSoulsClasses.warrior.level
        adventurer.strength = TextSoulsClasses.warrior.strength
        adventurer.vitality = TextSoulsClasses.warrior.vitality
        adventurer.endurance = TextSoulsClasses.warrior.endurance
        adventurer.dexterity = TextSoulsClasses.warrior.dexterity
        adventurer.gold = TextSoulsClasses.warrior.gold
        adventurer.souls = TextSoulsClasses.warrior.souls
        area_FirelinkShrine.firelink_shrine()
    else :
        game_over()




character_creation()